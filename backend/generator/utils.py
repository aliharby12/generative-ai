from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()


def generate_response(prompt: str) -> str:
    """
    Generate a response using OpenAI's GPT model based on the provided prompt.

    Args:
        prompt (str): The user's input prompt.

    Returns:
        str: The response from the AI model.
    """
    try:
        # Create the completion
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        # Extract and return the response message
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


def generate_image(
    prompt: str, size: str = "1024x1024", quality: str = "standard", n: int = 1
) -> str:
    """
    Generate an image using OpenAI's DALL-E model based on the provided prompt.

    Args:
        prompt (str): The description of the image to generate.
        size (str): The size of the generated image (e.g., "1024x1024").
        quality (str): The quality of the generated image ("standard" or other options).
        n (int): The number of images to generate.

    Returns:
        str: The URL of the generated image or an error message.
    """
    try:
        # Generate the image
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size=size,
            quality=quality,
            n=n,
        )
        # Extract and return the URL of the first generated image
        return response.data[0].url
    except Exception as e:
        return f"An error occurred: {str(e)}"
