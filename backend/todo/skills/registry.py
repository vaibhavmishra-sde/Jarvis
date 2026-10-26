"""Small registry for assistant capabilities.

Each skill is metadata-first so a future tool-calling adapter can expose the
same contract to an OpenAI-compatible model without coupling it to the views.
"""

SKILLS = {
    'time': {
        'name': 'time',
        'description': 'Get the current local time and date.',
        'parameters': {},
    },
    'web_search': {
        'name': 'web_search',
        'description': 'Create a safe web search link for a query.',
        'parameters': {'query': {'type': 'string', 'required': True}},
    },
    'youtube_search': {
        'name': 'youtube_search',
        'description': 'Find a video or music query on YouTube.',
        'parameters': {'query': {'type': 'string', 'required': True}},
    },
    'add_todo': {
        'name': 'add_todo',
        'description': 'Add an item to the user to-do list.',
        'parameters': {'title': {'type': 'string', 'required': True}},
    },
    'set_reminder': {
        'name': 'set_reminder',
        'description': 'Set a reminder for a future time.',
        'parameters': {'title': {'type': 'string', 'required': True}, 'minutes': {'type': 'integer', 'required': True}},
    },
}


def list_skills():
    return list(SKILLS.values())


def get_skill(name):
    return SKILLS.get(name)
