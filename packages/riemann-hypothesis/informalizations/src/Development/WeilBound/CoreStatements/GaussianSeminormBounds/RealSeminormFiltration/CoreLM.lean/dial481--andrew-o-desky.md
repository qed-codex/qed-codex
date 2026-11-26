---
{
  "module": "src/Development/WeilBound/CoreStatements/GaussianSeminormBounds/RealSeminormFiltration/CoreLM.lean",
  "declarations": [
    "PositivityTheory.KReal.coreLM"
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

## A common irreducible quotient of two theta coinvariant modules

[Theorem THETA.1239](https://andrewodesky.com/rh/lean/PositivityTheory.KReal.coreLM/)

Let $a,a',p,q,\kappa\in\mathbb N$ satisfy $$a'<a,\quad 1\le a',\quad a-a'\equiv\kappa\equiv0\pmod2,$$ $$2p+1\le a,\quad2q+1\le a',\quad a+a'<\kappa,\quad2(p+q)<a',\quad2p+a'<a.$$ Put $R=a+a'-p-q$ and $S=p+q$. Write $\mathcal T_{u,v;R,S}(c)$ for the polynomial Fock module for the unitary pair of signatures $(u,v)$ and $(R,S)$, modulo the span of $Zf-c\operatorname{tr}(Z)f$ for the first Lie algebra. Let $$T=\mathcal T_{a-p,p;R,S}(\kappa/2),\qquad T'=\mathcal T_{q,a'-q;R,S}(-\kappa/2).$$ Use the second Fock Lie action on $T$; on $T'$ add the scalar operator $\frac\kappa2\operatorname{tr}(W)$ to that second action. There exist a nonzero complex vector space $\Pi$, operators $A_W\in\operatorname{End}_{\mathbb C}(\Pi)$ for $W\in M_{R+S}(\mathbb C)$, and surjective linear maps $T\to\Pi$, $T'\to\Pi$ intertwining these operators. Every subspace of $\Pi$ invariant under all $A_W$ is zero or $\Pi$.
