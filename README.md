### Talking Rubbish Podcast Summariser

#### Purpose 
To take a TTML transcript file (available from the Apple Podcast App) and output a summarised version of the key takeaways to share with a local neighbourhood recycling group.

#### Caveats 
Rubbish Talk is removed from the transcript to reduce the number of tokens passed to the prompt. 
The idea is not to summarise the full podcast, just to pull out some useful tips and tricks.
An Open API key is required to be present as an environment variable.


#### Running the script
The transcript to be summarised should be in ttml format, named `<episode number>.ttml` and placed in the transcripts folder. The script can be run from the command line - the episode number needs to be passed as the first and only positional argument. Here is an example command for running:
` uv run --env-file .env python main.py 75`
