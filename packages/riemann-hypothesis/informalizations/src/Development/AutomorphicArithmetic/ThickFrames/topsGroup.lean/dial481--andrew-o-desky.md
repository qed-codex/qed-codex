---
{
  "module": "src/Development/AutomorphicArithmetic/ThickFrames/topsGroup.lean",
  "declarations": [
    "UpperTheory.BernoulliSumsFrobeniusOrbits.topsGroup"
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

## A subset with prescribed coset frequencies and few bad cyclic orbits

[Theorem ALG.0542](https://andrewodesky.com/rh/lean/UpperTheory.BernoulliSumsFrobeniusOrbits.topsGroup/)

For every $\varepsilon>0$ and $C,L\in\mathbb R$, there are $C_b>0$ and $x_0\in\mathbb R$ with the following property for $x\ge x_0$. Let $A$ be a finite abelian group, $A_0\le A$, $d=[A:A_0]$, and $L_2\ge0$ an integer. Suppose $$\tfrac12x^h\le|A|\le Cx^h,\qquad d\le C,\qquad L_2\le L.$$ Let $b:A\times A\to A$ satisfy $b(a,t)\in t+\langle a\rangle$. Let $P\subseteq\mathbb N$ be finite, $a_p\in A$, and $\omega:\mathbb N\to[0,\infty)$, with $\operatorname{ord}(a_p)\ge x^{\varepsilon/4}$ for $p\in P$. There is $T\subseteq A$ satisfying $$\tfrac12\delta|A|\le|T|\le2\delta|A|,$$ $$\left||T\cap(\gamma+A_0)|-\frac{3+\mathbf1_{A_0}(\gamma)}{3d+1}|T|\right|\le x^{-1+\varepsilon}|T|\qquad(\gamma\in A),$$ and $$\sum_{p\in P}\omega(p)|B_p|\le4C_bx^{-2}\delta|A|\sum_{p\in P}\omega(p).$$ Here $B_p$ consists of those $t\in T$ for which $$S_{p,t}=\{0\le i<\operatorname{ord}(a_p):b(a_p,t)+ia_p\in T\}$$ fails one of the three conditions in the conventions below, with $n=\operatorname{ord}(a_p)$ and $S=S_{p,t}$.
