import requests

def stt():
    url = "https://api.sarvam.ai/speech-to-text-translate"
    api_key = "2eb08a65-79b8-450a-b1e1-2e0f38803075"
    audio_file_path = "/home/ubuntu/neuraoak/latest_recording.wav"

    files = {
        "file": ("output_audio_3.wav", open(audio_file_path, "rb"), "audio/wav")
    }

    data = {
        "model": "saaras:v2",
        "prompt": "The audio file is both in English as well as Telugu, so make sure to understand the context and translate to English.",
        "with_diarization": "false" 
    }
    headers = {
        "api-subscription-key":  api_key
    }

    # Send the POST request
    response = requests.post(url, files=files, data=data, headers=headers)

    response_json = response.json() 

    transcript = response_json.get("transcript", "No transcript available")

    print("Transcript:", transcript)
    return transcript