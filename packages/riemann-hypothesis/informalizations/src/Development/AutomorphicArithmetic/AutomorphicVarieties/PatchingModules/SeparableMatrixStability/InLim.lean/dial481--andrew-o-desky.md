---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules/SeparableMatrixStability/InLim.lean",
  "declarations": [
    "UpperTheory.V.Pa.in_lim"
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

## A limiting homomorphism into a quotient of a compact group

[Theorem ALG.1110](https://andrewodesky.com/rh/lean/UpperTheory.V.Pa.in_lim/)

Let $\Phi,Y,\Gamma_N$ be compact totally disconnected topological groups. Let $\pi_N:\Phi\to\Gamma_N$ be continuous surjective homomorphisms, $\mathcal U$ an ultrafilter on $\mathbb N$, and $P\triangleleft Y$ such that $Y/P$ is topologically finitely generated. Let $f_N:Y\to\Gamma_N$ be continuous homomorphisms with $P\subseteq\ker f_N$. Put $$K=\{g\in\Phi:\text{for every open normal }V\subseteq\Phi,\ g\in(\ker\pi_N)V\text{ for }\mathcal U\text{-almost every }N\}.$$ There exists a continuous homomorphism $F:Y\to\Phi/K$ such that for every open normal $V\subseteq\Phi$, for $\mathcal U$-almost every $N$ and every $y\in Y$, there are $g,g'\in\Phi$ with $$\pi_N(g)=f_N(y),\quad g'K=F(y),\quad g^{-1}g'\in V.$$
