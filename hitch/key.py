from hitchstory import HitchStoryException, StoryCollection
from hitchrun import expected
from commandlib import CommandError
from strictyaml import Str, Map, Bool, load
from pathquery import pathquery
from hitchrun import DIR
import dirtemplate
import hitchpylibrarytoolkit
from path import Path
from engine import Engine
import json


toolkit = hitchpylibrarytoolkit.ProjectToolkit(
    "hitchdocker",
    DIR,
)


@expected(HitchStoryException)
def bdd(*keywords):
    """Run single story."""
    toolkit.bdd(Engine(toolkit.build), keywords)
    

@expected(HitchStoryException)
def regression():
    """Run all stories."""
    clean()
    toolkit.regression(Engine(toolkit.build))


@expected(CommandError)
def clean():
    """Clean out builds."""
    DIR.gen.joinpath("py3.7.0").rmtree(ignore_errors=True)


def deploy(version):
    """
    Deploy to pypi as specified version.
    """
    toolkit.deploy(version)

    
