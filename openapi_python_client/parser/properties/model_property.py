from dataclasses import dataclass
from typing import ClassVar, List, Set

from ..reference import Reference
from .property import Property


@dataclass
class ModelProperty(Property):
    """ A property which refers to another Schema """

    reference: Reference

    required_properties: List[Property]
    optional_properties: List[Property]
    description: str
    relative_imports: Set[str]

    template: ClassVar[str] = "ref_property.pyi"
    # TODO: change to model_property.pyi

    def get_type_string(self, no_optional: bool = False) -> str:
        """ Get a string representation of type that should be used when declaring this property """
        if no_optional or (self.required and not self.nullable):
            return self.reference.class_name
        return f"Optional[{self.reference.class_name}]"

    def get_imports(self, *, prefix: str) -> Set[str]:
        """
        Get a set of import strings that should be included when this property is used somewhere

        Args:
            prefix: A prefix to put before any relative (local) module names. This should be the number of . to get
            back to the root of the generated client.
        """
        imports = super().get_imports(prefix=prefix)
        imports.update(
            {
                f"from {prefix}models.{self.reference.module_name} import {self.reference.class_name}",
                "from typing import Dict",
                "from typing import cast",
            }
        )
        return imports
