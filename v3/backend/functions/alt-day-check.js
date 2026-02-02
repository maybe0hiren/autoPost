function altDayCheck() {
    const day = new Date().getDate();
    if (day%2) {
        return true;
    }
    return false;
}

exports.altDayCheck = altDayCheck;