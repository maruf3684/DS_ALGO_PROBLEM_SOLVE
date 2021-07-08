//! Async function always return promise
//! await keyword sobsomoy use hoi asinc function er vitore , bahire noy

//? await ki kore? asyncronas kaj done houae jonno wait kore


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


const calenderMake=(meetingDetails)=>{
       let calender=`${meetingDetails.name} has 31 tarikh calender date`
       return Promise.resolve(calender)
}



(async function details(){
    try{
  let meetingDetails2=await meeting;
  let calender2=await calenderMake(meetingDetails2)
  console.log(meetingDetails2,calender2);
}catch(e){
    console.log(e);
}
}())

console.log("1st print");