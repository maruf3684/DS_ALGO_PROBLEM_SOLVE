
let HasMeeting=true;
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


const calenderMake=(meetingDetails)=>{
       let calender=`${meetingDetails.name} has 31 tarikh calender date`
       return Promise.resolve(calender)
}


meeting.then(calenderMake)  //!alenderMake er paramiter hobe resolve er data
.then((resolveValue)=>{console.log(resolveValue)})
.catch((rejectValue)=>{console.log(rejectValue.message)})
