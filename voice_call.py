import os
import speech_recognition as sr
from twilio.rest import Client

def transcribe_voice_call(to_number, from_number, twilio_sid, twilio_auth_token, recording_file):
    # Make the voice call
    client = Client(twilio_sid, twilio_auth_token)
    call = client.calls.create(
        twiml='<Response><Say>Hello, this is a test voice call.</Say></Response>',
        to=to_number,
        from_=from_number,
        record=True
    )

    print("Call SID:", call.sid)

    # Wait for the call to complete
    call = call.fetch()
    recording_sid = call.recording.sid
    recording_url = call.recording.url

    print("Recording URL:", recording_url)

    # Download the recording
    client.recordings.get(recording_sid).download(recording_file)

    # Transcribe the recording
    r = sr.Recognizer()
    with sr.AudioFile(recording_file) as source:
        audio = r.record(source)

    # Perform speech recognition
    try:
        transcription = r.recognize_google(audio)
        print("Transcription:", transcription)

        # Save the transcription
        transcription_file = "transcription.txt"
        with open(transcription_file, "w") as f:
            f.write(transcription)

        print("Transcription saved to:", transcription_file)

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))

# Usage example:
to_number = "RECIPIENT_PHONE_NUMBER"
from_number = "YOUR_TWILIO_PHONE_NUMBER"
twilio_sid = "YOUR_TWILIO_SID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
recording_file = "recording.wav"

transcribe_voice_call(to_number, from_number, twilio_sid, twilio_auth_token, recording_file)