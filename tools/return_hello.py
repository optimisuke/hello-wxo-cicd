from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def return_hello(name: str) -> str:
    """
    Returns a greeting with the provided name

    :param name: The name to include in the greeting
    :returns: A greeting string in the format "Hello [name]"
    """

    return "Hi " + name
