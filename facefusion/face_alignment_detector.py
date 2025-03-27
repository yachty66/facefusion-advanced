import os
import cv2
from litellm import completion
import base64
from dotenv import load_dotenv
import json

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def get_alignment_of_faces(vision_frame) -> str:
	#!only temporarly for testing in prod the vision frame will be no path
	vision_frame = cv2.imread(vision_frame)

	# Convert frame to PNG in memory and encode to base64
	_, buffer = cv2.imencode('.png', vision_frame)
	base64_image = base64.b64encode(buffer).decode('utf-8')

	prompt="""
	Analyze the image and determine if the person is positioned horizontally or vertically. 

	Based on your observations, classify the person's position as either "horizontal" or "vertical" and keep your response to a minimum really briefly.
	"""

	# Make API call to vision model
	response = completion(
		model="gpt-4o-mini",
		messages=[
			{
				"role": "user",
				"content": [
					{
						"type": "text",
						"text": prompt
					},
					{
						"type": "image_url",
						"image_url": {
							"url": f"data:image/jpeg;base64,{base64_image}"
						}
					}
				]
			}
		],
	)
	return response.choices[0].message.content

#extract the result from the response
def extract_result(response: str) -> str:
	prompt = f"""
	You are processing the output from an image orientation detection system. Extract ONLY the orientation value based on these rules:
	- If the detection result clearly indicates a person in a horizontal position: return 1
	- If the detection result clearly indicates a person in a vertical position: return 2
	- For any unclear result, no person detected, or ambiguous response: return 0

	Here is the detection result to analyze:
	{response}

	Respond with ONLY a JSON object containing a single key "value" with value 1, 2, or 0.
	"""
	response = completion(
    	model = "gpt-4o-mini", 
		response_format={ "type": "json_object" },
    	messages=[{ "content": prompt,"role": "user"}],
		temperature=0.0
	)
	response_json = json.loads(response.choices[0].message.content)
	#how to make sure that the model really only responds with one value ie 90 or 270 or 0?
	return response_json["value"]