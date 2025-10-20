import React, {useState} from 'react';

import {supabase} from '../supabaseClient';
import './MainPage.css'

function MainPage(){
    const [task, setTask] = useState('');
    const [image, setImage] = useState([]);
    const [uploading, setUploading] = useState(false);
    const [updates, setUpdates] = useState("Hello There...")

    async function uploadHandler(){
        if (!task){
            setTask(" ");
        }
        setUploading(true);
        try{
            const uploadedImageURLS = [];
            for(const file of image){
                const fileExtension = file.name.split('.').pop();
                const fileName = `${Date.now()}-${Math.random().toString(36).substring(2)}.${fileExtension}`;

                //Upload an Image to the Supabase storage bucket & Show error if any
                const {error: uploadingError} = await supabase.storage.from('images').upload(fileName, file);
                if(uploadingError){
                    setUpdates(`Error: ${uploadingError}`);
                    continue;
                } 
                //Get image url from the bucket
                const {data} = supabase.storage.from('images').getPublicUrl(fileName);
                uploadedImageURLS.push(data.publicUrl);
            }

            //Insert the URL along with task into table & show error if any
            const {error: insertionError} = await supabase.from('postContent').insert([{task, imageURLs:uploadedImageURLS}]);
            if(insertionError){
                setUpdates(`Error: ${insertionError}`);
            }

            setUpdates('Upload successful!')
            setTask('');
            setImage([]);
        } catch (error) {
            setUpdates('Error:', error.message)
        } finally {
            setUploading(false)
        }
    }
    return(
        <>
        <div id='submission'>
            <input type='text' placeholder='Enter task' value={task} onChange={(e) => setTask(e.target.value)} />
            <br />
            <input type='file' accept='image/*' onChange={(e) => setImage(Array.from(e.target.files))}/>
            <br />
            <button onClick={uploadHandler} disabled={uploading || (!task && image.length === 0)}>{uploading ? "Uploading..." : "Upload"}</button>
            <p id='display'>{updates}</p>
        </div>
        </>
    );
}

export default MainPage;


