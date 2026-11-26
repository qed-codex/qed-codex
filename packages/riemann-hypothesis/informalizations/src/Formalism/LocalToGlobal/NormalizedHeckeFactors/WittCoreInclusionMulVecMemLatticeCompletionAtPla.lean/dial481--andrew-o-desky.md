---
{
  "module": "src/Formalism/LocalToGlobal/NormalizedHeckeFactors/WittCoreInclusionMulVecMemLatticeCompletionAtPla.lean",
  "declarations": [
    "Formalism.L2.NTwTied",
    "Formalism.L2.TwFrame"
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

## Local coefficient rings and normalized twists

[Definition / hypothesis ARAK.D226](https://andrewodesky.com/rh/lean/Formalism.L2.TwFrame/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)), ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)), ([Finite types and idempotents for the family](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NTypes/)), and ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)). Write $K_0$ for the fixed coefficient subfield, $O_i^0,O_i,O_{i,k}$ for the coefficient rings at twist index $i$, and $\ell=\ell_i$.

Hypothesis (concrete twist coefficient rings). Choose finite extensions $L_i^0,L_i^1\subseteq\overline{\mathbb Q}_\ell$ and an embedding $j_i:K_0\hookrightarrow\overline{\mathbb Q}_\ell$. Put $$F_i=L_i^0L_i^1\mathbb Q_\ell^{\rm unr},\qquad F_{i,k}=F_i(\mu_{\ell^k}).$$ For a subfield $F$ of $\overline{\mathbb Q}_\ell$, let $\overline{\mathcal O}(F)$ be the intersection of $\mathcal O_{\mathbb C_\ell}$ with the topological closure of $F$ in $\mathbb C_\ell$. Choose ring isomorphisms $$O_i^0\simeq\mathcal O_{L_i^0},\qquad O_i\simeq\overline{\mathcal O}(F_i),\qquad O_{i,k}\simeq\overline{\mathcal O}(F_{i,k}),$$ a complex embedding $c_i:\operatorname{Frac}(O_i)\hookrightarrow\mathbb C$, and a finite extra excluded-prime set $S_i^x$.

The base integer-ring isomorphism agrees with the standard $\mathbb Z_\ell$ embedding. The twist-ring isomorphism extends it, and every extended-ring isomorphism extends the twist-ring isomorphism. The true-side embedding $K_0\to\operatorname{Frac}(O_i^0)$ induces a prime $\lambda_i$ above $\ell$: an integral $x\in K_0$ lies in $\lambda_i$ exactly when its image is represented by an element of the maximal ideal of $O_i^0$. It agrees with $j_i$ under the first ring isomorphism in the following exact fraction sense. For all $x\in K_0$ and $y,z\in O_i^0$ with $z\ne0$, $$e_i^0(x)z=y\quad\Longleftrightarrow\quad j_i(x)e_i^0(z)=e_i^0(y),$$ where on the right $e_i^0$ denotes the chosen integer-ring isomorphism and on the left the recorded fraction-field embedding. If $\ell=g_0$ or $g_1$, then $\mu_\ell\subseteq F_i$.

The full excluded set is exactly $$S_{0,i}=\{P:P\mid\ell g_0g_1p_\Delta p'_{\Delta}\}\cup S_i^x.$$ The extra set is closed under CM conjugation and contains every prime over two, over the auxiliary prime $q_0$ defined in ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)), over a rational divisor of $N\mathfrak c_{E_0}$, or over a rational divisor of $|\operatorname{disc}E|$.

At every natural stage, side and Hecke index, and every $P\notin S_{0,i}$, the recorded integral Hecke characteristic polynomial splits over $\operatorname{Frac}(O_i)$. For every such $P$ and every abelian theta label $\lambda$, the recorded normalization scalar satisfies $$c_i(q_{i,\lambda,P})=(NP)^{-s_{i,\lambda}/2}.$$ The image of the chosen integral $B$-module in the theta-form space is exactly the intersection of its specified ambient integral module with the selected finite-type idempotent image of the level-character eigenspace. Finally, two spectral labels with the same stage, the same side and identical Hecke eigenvalues at every split $P\notin S_{0,i}$ and $1\le k\le r$ are equal.
