# vim: set fileencoding=utf-8
"""
pythoneda/artifact/shared/banner/banner_nix_flake.py

This file defines the BannerNixFlake class.

Copyright (C) 2024-today rydnr's pythoneda-shared-pythonlang-artf/banner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.artifact.external.flakeutils import FlakeUtilsNixFlake
from pythoneda.artifact.external.nixpkgs import NixpkgsNixFlake
from pythoneda.shared.nix.flake import NixFlake


class BannerNixFlake(NixFlake):

    """
    Nix flake for pythoneda-shared-pythonlang/banner.

    Class name: BannerNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared-pythonlang/banner.
        - Provides a way to run pythoneda-shared-pythonlang/banner.

    Collaborators:
        - pythoneda.shared.nix.flake.NixFlake
    """

    def __init__(self, version: str):
        """
        Creates a new BannerNixFlake instance.
        :param version: The version.
        :type version: str
        """
        super().__init__(
            "pythoneda-shared-pythonlang-banner",
            version,
            "github:pythoneda-shared-pythonlang-def/banner/{version}",
            [FlakeUtilsNixFlake.default(), NixpkgsNixFlake.default()],
            "pythoneda",
            "Banner for PythonEDA projects",
            "https://github.com/pythoneda-shared-pythonlang/banner",
            "gpl3",
            ["rydnr <github@acm-sl.org>"],
            2023,
            "rydnr",
        )

    @classmethod
    def default(cls):
        """
        Retrieves the default version of the pythoneda-shared/banner Nix flake input.
        :return: Such instance.
        :rtype: pythoneda.shared.nix.flake.BannerNixFlake
        """
        return cls("0.0.49")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
