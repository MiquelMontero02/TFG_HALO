/*Gobal DOM change listener that control every template change*/
document.addEventListener("DOMContentLoaded",()=>{
  if (document.getElementById("profileSamples")) {
    loadProfileData();
  }
  if (document.getElementById("step-by-step")){
    setFormsEnv()
  }
  if(document.getElementById("SummaryCardNav")){
    initSummary()
  }   
  /*TO DO: Create a Sample View with OpenStreet Map */
  if(document.getElementById("sampleDataAmp")){
    
  }
} );
