# pythoneda-shared-pythonlang-artf/banner

Artifact for pythoneda-shared-pythonlang/banner

## How to declare it in your flake

python ~/github/pythoneda/pythoneda-tools-artifact/new-domain/pythoneda/tools/artifact/new_domain/application/new_domain_app.py -o pythoneda-shared-python -n shell -t "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" -g "D8DF2D915F27510072DFF42160856541692CA3C3" -p pythoneda.shared.shellox.removeme -d 'shared domain for shell operations'
Check the latest tag of the definition repository: https://github.com/pythoneda-shared-pythonlang-artf-def/banner, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-pythonlang-artf-banner = {
      [optional follows]
      url =
        "github:pythoneda-shared-pythonlang-artf-def/banner/[version]";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is managed by the [https://github.com/pythoneda-shared-pythonlang-artf-def/banner](banner "banner") definition repository.

Use the specific package depending on your system (one of `flake-utils.lib.defaultSystems`) and Python version:

- `#packages.[system].pythoneda-shared-pythonlang-artf-banner-python38`
- `#packages.[system].pythoneda-shared-pythonlang-artf-banner-python39`
- `#packages.[system].pythoneda-shared-pythonlang-artf-banner-python310`
- `#packages.[system].pythoneda-shared-pythonlang-artf-banner-python311`
