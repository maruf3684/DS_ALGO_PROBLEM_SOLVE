

let HasMeeting=false;
const meeting=new Promise((resolve,reject) => {
    if(HasMeeting==true){
        const meetingDetails={
                             name:"company meeting",
                             location:"dhaka"
                             };
        resolve(meetingDetails)
    }else{
        reject(new Error("NO MEETING AVAILABLE"))
    }
    
});

meeting.then((resolveValue)=>{console.log(resolveValue)}).catch((rejectValue)=>{console.log(rejectValue.message)})