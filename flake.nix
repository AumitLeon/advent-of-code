{
  description = "Python environment for advent of code 2024";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python312;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Python and uv package management
            python
            uv

            # Development tools
            ruff # Fast Python linter and formatter
            pre-commit

            # Language server
            python.pkgs.python-lsp-server

            # C++ standard library for numpy and scipy
            stdenv.cc.cc.lib
          ];

          shellHook = ''
            # Add C++ standard library to LD_LIBRARY_PATH for numpy/scipy
            export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH"

            echo "🐍 Python development environment with uv 🐍"
            echo "Python version: $(python --version)"
            echo "uv version: $(uv --version)"
            echo ""

            # Auto-activate virtual environment if it exists
            if [ -d ".venv" ]; then
              echo "✓ Activating virtual environment (.venv)"
              source .venv/bin/activate

              # Ensure nix tools (ruff, pre-commit) take precedence over venv versions
              # This fixes issues with dynamically linked binaries on NixOS
              export PATH="${pkgs.ruff}/bin:${pkgs.pre-commit}/bin:$PATH"
            else
              echo "ℹ No virtual environment found. Create one with:"
              echo "  uv sync    # Creates venv, lockfile, and installs dependencies"
            fi
          '';
        };
      }
    );
}
