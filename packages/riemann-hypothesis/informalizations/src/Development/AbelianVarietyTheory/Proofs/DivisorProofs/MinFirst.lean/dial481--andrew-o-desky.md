---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/MinFirst.lean",
  "declarations": [
    "GlobalTheory.FockAlg.min_first"
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

## Joint harmonics detect a compact type of minimal degree

[Theorem REP.0336](https://andrewodesky.com/rh/lean/GlobalTheory.FockAlg.min_first/)

Let $p,q,r,s\ge0$, $I=\{1,\ldots,p\}\sqcup\{1,\ldots,q\}$ and $J=\{1,\ldots,r\}\sqcup\{1,\ldots,s\}$. Let $M_1,M_2$ be modules for $\mathfrak{gl}_{p+q}(\mathbb C),\mathfrak{gl}_{r+s}(\mathbb C)$, locally finite under their block-diagonal subalgebras and spanned by rational diagonal-weight vectors. Assume $M_1$ is nonzero and irreducible, and every compact highest-weight space of $M_1$ is finite-dimensional.

Let $\mathcal P=\mathbb C[X_{ij}:i\in I,j\in J]$ carry the two Fock actions $A_1,A_2$ in the conventions, and let $$0\ne f:\mathcal P\longrightarrow M_1\otimes_{\mathbb C}M_2$$ be linear, intertwining $A_1$ with the first tensor factor and $A_2$ with the second. Let $\mu\in\mathbb Q^I$ occur as a compact highest weight in $M_1$ and minimize $$d(\nu)=\sum_{i\text{ in first block}}|\nu_i-(r-s)/2|+\sum_{i\text{ in second block}}|\nu_i+(r-s)/2|$$ among all such highest weights $\nu$. There are $\mu'\in\mathbb Q^J$ and a jointly harmonic polynomial $P$ which is a compact highest-weight vector of weights $\mu,\mu'$ for $A_1,A_2$ respectively, with $f(P)\ne0$. Moreover, if $P$ has compact type $\mu$ for $A_1$, then $$f(P)\in f\bigl(\langle Q:Q\text{ is jointly harmonic and has compact type }\mu\rangle_{A_2}\bigr),$$ where $\langle\cdot\rangle_{A_2}$ is the smallest linear subspace containing the indicated polynomials and stable under every $A_2(Y)$.
