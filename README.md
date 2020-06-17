# Workflows

Your are tasked with creating a simple version of an HTTP API for a workflow system. The important entities are *workflow* and
*comment*.

A *workflow* is a series of ordered steps to be followed in order to achieve a result. It has a name,
a description and a set of ordered steps. A step has a name and a description.
 
A *comment* is a message left by someone about a workflow. A comment has the name of the person who posted and the
text of the comment.

The API should allow for retrieving, listing, creating, updating and deleting workflows and comments. The order of the
steps is important and should be preserved.

An example of a json to create a workflow would be:

```json
{
    "name": "How to nail something",
    "description": "Basic instructions to nail something",
    "steps": [
      {
         "name": "Place nail",
         "description": "Hold nail on top the thing to be nailed"
      },
      {
        "name": "Hit nail",
        "description": "Hit the nail repeatedly with a hammer"
      }   
    ]
}
``` 

An example of a json to create a comment of a workflow would be:

```json
{
  "name": "Concerned  person",
  "text": "On the step 'Hit Nail' be careful to not hit your hand!"
}
```

Use Django (https://www.djang oproject.com) and Django Rest Framework (https://www.django-rest-framework.org/), you can use any database you would like.
Clean code and code organization and unit tests are important.

Provide also an Open API 3 (https://github.com/OAI/OpenAPI-Specification/blob/3.0.3/versions/3.0.0.md) spec for the API.

You should deliver a git repository with your code, and a short README file explaining how to build, run and use it.

Some useful links:
 * A guide for Django in Visual Studio Code https://code.visualstudio.com/docs/python/tutorial-django
 * A python IDE https://www.jetbrains.com/pycharm/download/

Feel free to contact us about question regarding the project.
