"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [17, [1, 3, 4]],
            "answer": 2
        },
        {
            "input": "123*45#=5#088",
            "answer": 6
        }
    ],
    "Extra": [
        {
            "input": "-5#*-1=5#",
            "answer": 0
        },
        {
            "input": "##*##=302#",
            "answer": 5
        },
        {
            "input": "#*11=##",
            "answer": 2
        },
        {
            "input": "19--45=5#",
            "answer": -1
        }

    ]
}
