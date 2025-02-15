const twilio = require("twilio");

const accountSid = "AC967a7aee91b0ca9cf47d299f696777d3"; // Twilio Account SID
const authToken = "1e18ffb5985f99525a05bd9487be5f6d"; // Twilio Auth Token
const twilioNumber = "+18572715353"; // Your Twilio Phone Number

const client = twilio(accountSid, authToken);

async function createCall() {
  try {
    const call = await client.calls.create({
      from: twilioNumber,
      to: "+916303105509", // Replace with the actual number
      record: true,
      url: "https://7b87-13-202-216-63.ngrok-free.app/twiml-response",
      method:"GET", // FastAPI endpoint for TwiML
      //recordingStatusCallback: "https://0896-13-202-216-63.ngrok-free.app/twilio-webhook", // Webhook for recording URL
      //recordingStatusCallbackMethod: "POST",
      
    });

    console.log("Call initiated! SID:", call.sid);
  } catch (error) {
    console.error("Error making the call:", error.message);
  }
}

createCall();