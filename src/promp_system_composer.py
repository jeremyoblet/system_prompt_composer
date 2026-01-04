from pathlib import Path
from typing import List, Dict, Iterable, Optional

import tiktoken



class PromptSystemComposer():
    def __init__(self):
        pass

    def _list_md_files(self, root: Path) -> List[Path]:
        """
        Parcourt récursivement `root` et retourne la liste des fichiers .md trouvés.
        """
        root = root.resolve()
        if not root.exists() or not root.is_dir():
            raise FileNotFoundError(f"Chemin invalide: {root}")

        return [p for p in root.rglob("*.md") if p.is_file()]
    
    def _read_md_files(self, md_files: Iterable[Path]) -> Dict[str, str]:
        """
        Lit le contenu de chaque fichier .md fourni.

        Retour:
        dict[str, str]
            clé   = nom du fichier sans extension (ex: "prompt")
            valeur = contenu du fichier
        """
        contents: Dict[str, str] = {}

        for path in md_files:
            if not path.exists() or not path.is_file():
                raise FileNotFoundError(f"Fichier invalide: {path}")

            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = path.read_text(encoding="utf-8-sig")

            key = path.stem  # nom du fichier sans extension
            contents[key] = text

        return contents
    
    def concat_by_keys(
        self,
        contents: Dict[str, str],
        keys: Iterable[str],
        *,
        separator: str = "\n\n"
    ) -> str:
        """
        Concatène les valeurs du dictionnaire `contents` selon l'ordre des `keys`.

        Paramètres:
        contents : dict[str, str]
            clé -> contenu
        keys : iterable[str]
            liste ordonnée des clés à concaténer
        separator : str
            séparateur entre chaque bloc

        Retour:
        str : string concaténée finale
        """
        parts = []

        for key in keys:
            if key not in contents:
                raise KeyError(f"Clé absente du dictionnaire: '{key}'")
            parts.append(contents[key].strip())

        return separator.join(parts)

    def count_tokens(self, text: str, model: str = "gpt-4o-mini") -> int:
        """
        Compte le nombre de tokens LLM pour une string donnée.

        Paramètres:
        text : str
            Texte à analyser
        model : str
            Modèle cible (impacte le tokenizer)

        Retour:
        int : nombre de tokens
        """
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))

if __name__ == "__main__":
    PROMPTS_DIR = Path(r"C:\Users\Wam\Documents\CODING\IA\system_prompt_composer\prompts")
    wanted_prompts = ['coder', 'conception']

    psc = PromptSystemComposer()
    files = psc._list_md_files(PROMPTS_DIR)
    extracted_prompts = psc._read_md_files(files)
    output = psc.concat_by_keys(extracted_prompts, wanted_prompts)

    print(output)

    tokens = psc.count_tokens(output, 'gpt-4o')
    print(tokens)