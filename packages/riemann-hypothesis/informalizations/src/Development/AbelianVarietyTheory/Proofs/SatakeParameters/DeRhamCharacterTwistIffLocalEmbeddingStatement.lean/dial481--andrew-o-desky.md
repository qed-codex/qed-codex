---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/DeRhamCharacterTwistIffLocalEmbeddingStatement.lean",
  "declarations": [
    "GlobalTheory.T.deRham_characterTwist_iff_localEmbedding"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A de Rham character preserves the de Rham condition under twisting

[Theorem PHT.0721](https://andrewodesky.com/rh/lean/GlobalTheory.T.deRham_characterTwist_iff_localEmbedding/)

Let $p$ be prime and fix a realization of the local period rings tied to Fontaine's rings as specified below. Let $E\subseteq\Omega$ be fields and let $G\subseteq\operatorname{Aut}_E(\Omega)$. Fix the local Galois bridge described below. Let $$r:G\to\operatorname{GL}_a(\overline{\mathbb Q}_p),\qquad c:G\to\operatorname{GL}_1(\overline{\mathbb Q}_p)$$ be continuous in their matrix entries. If $c$ is de Rham relative to this bridge, then $$r\otimes\det c\text{ is de Rham}\quad\Longleftrightarrow\quad r\text{ is de Rham}.$$
