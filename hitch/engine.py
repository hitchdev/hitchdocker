from hitchstory import InfoDefinition, InfoProperty
from strictyaml import Seq, Enum
import hitchpylibrarytoolkit


class Engine(hitchpylibrarytoolkit.Engine):
    info_definition = InfoDefinition(
        status=InfoProperty(Seq(Enum([
            "stable", "experimental"
        ]))),
    )
        
    def set_up(self):
        super().set_up()

