from pydantic_ai import Agent
from model import nvidia_model

movie_agent = Agent(model=nvidia_model("nvidia/nemotron-3.5-super-vl-120b-a12b"), 
                    instructions="You are an expert in finding a movie based on a text")


# be able to run as standalone script
# __name__ is '__main__' when run directly
# __name__ is 'agents' when imported
if __name__ == "__main__":

    # to test an agent in python script -> use run_sync
    movie = movie_agent.run_sync("I'll be back")
    print(movie)

