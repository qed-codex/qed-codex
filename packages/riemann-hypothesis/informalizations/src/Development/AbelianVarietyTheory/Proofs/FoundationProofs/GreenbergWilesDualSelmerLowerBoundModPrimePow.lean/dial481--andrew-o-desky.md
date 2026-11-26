---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/GreenbergWilesDualSelmerLowerBoundModPrimePow.lean",
  "declarations": [
    "GlobalTheory.Ord2.GwIneq.gw_ineq"
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

## A uniform comparison with a dual ordinary Selmer family

[Theorem GC.0639](https://andrewodesky.com/rh/lean/GlobalTheory.Ord2.GwIneq.gw_ineq/)

Assume ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)). Let $\ell$ be an odd prime, let $\Omega$ be an algebraic closure of $\mathbb Q$, and write $\chi_\ell$ for the $\ell$-adic cyclotomic character. Let $$W:G_{\mathbb Q}\to\operatorname{GL}_2(\overline{\mathbb Q}_\ell)$$ be continuous. Fix $e\ge1$, a finite set $S$ of rational finite primes containing $\ell$, and a place of $\Omega$ above $\ell$, with decomposition group $D_\ell$ and inertia $I_\ell$. Suppose $W$ is unramified outside $S$, has matrices in some coefficient ring finite over $\mathbb Z_\ell$, and satisfies $$\det(W)^2=1,\qquad\det(W(c))=-1\text{ for every complex conjugation }c.$$ Assume its restriction to $\ker\chi_\ell\cap\ker\det W$ is irreducible. On $D_\ell$, assume $W$ is upper triangular and, for some $m\ge1$, $$W_{11}(\sigma)^m=\chi_\ell(\sigma)^{em}\qquad(\sigma\in I_\ell).$$ Require also some $\sigma\in D_\ell$ with $W_{11}(\sigma)\ne\chi_\ell(\sigma)$.

Let $O\subseteq\overline{\mathbb Q}_\ell$ be a discrete valuation $\mathbb Z_\ell$-subalgebra finite over $\mathbb Z_\ell$, containing every matrix entry of $W$. Put $W^*=W\otimes\chi_\ell(\det W)^{-1}$. There is an integer $C\ge0$ such that, for every $n\ge1$ and every finite family of $N$ pairwise noncohomologous cochains in $\mathcal S_n(W)$, there is a family of $N'$ pairwise noncohomologous cochains in $\mathcal S_n(W^*)$ with $$N\le CN'.$$
