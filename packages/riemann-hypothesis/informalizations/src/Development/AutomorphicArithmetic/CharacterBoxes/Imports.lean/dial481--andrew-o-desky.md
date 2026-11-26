---
{
  "module": "src/Development/AutomorphicArithmetic/CharacterBoxes/Imports.lean",
  "declarations": [
    "UpperTheory.Top.admitted"
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

## Field conditions at an integer and the completion property of an abelian CM field with reciprocity map

[Definition / hypothesis ANT.D273](https://andrewodesky.com/rh/lean/HostParam.Seam.FieldRows/)

Let $\mathfrak E$ be data that satisfy Hypothesis (abelian CM field with reciprocity map) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). The notation is that of this entry: the group $A$ of order $n$, the integer $e$, the element $a_0$ of order $n_0$ and the index $o=n/n_0$; the primes $q$ and $d$, the integer $Q_S$ and $Q=Q_Sqd$; the field $E$ with the automorphisms $\sigma_g$ for $g\in G=\{\pm1\}^2\times A$; and the homomorphism $\alpha:(\mathbb Z/Q\mathbb Z)^\times\to G$ with its first sign coordinate $\operatorname{pr}_q\alpha$.

**Field conditions.** Let $b\ge0$ be an integer. The data $\mathfrak E$ *satisfy the field conditions at $b$* when the following eight conditions hold.

1. $\operatorname{pr}_q\alpha(u)=\left(\frac uq\right)$ for every $u\in(\mathbb Z/Q\mathbb Z)^\times$.
2. There is $s_q\in E$ with $s_q^2=-q$ and $\sigma_{(\epsilon_q,\epsilon_d,a)}s_q=\epsilon_qs_q$ for every $(\epsilon_q,\epsilon_d,a)\in G$.
3. For every prime $\ell\mid Q_S$ there is $u\in(\mathbb Z/Q\mathbb Z)^\times$ with $u\equiv1\pmod{Q/\ell}$ and $\alpha(u)\ne1_G$.
4. $Q_S\le n^2$.
5. $o^{64}\le2^e$.
6. $q\ne3$.
7. $\left(\frac{-d}p\right)=1$ for every odd prime $p\le b$.
8. $4\ell\le b$ for every odd prime $\ell\mid Q_S$.

These are the requirements of Hypothesis (fields and Galois data) of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) that involve only $\mathfrak E$ and the integer $s_0$ of that hypothesis, with $s_0=b$, except the requirement $q,d>4tr+1$.

**Completion property.** Let $k,m,t$ be natural numbers that satisfy the parity conditions and the inequalities required of them in Hypothesis (fields and Galois data), and put $r=k+m-1$. A *choice of the remaining data* for $\mathfrak E$ consists of the set $\mathcal P_{\rm lev}$, the primes $g_0,g_1,p_\Delta,p'_\Delta$, the ideal $\mathfrak c$, the sets $T$ and $T_2$, the shift $a_*$, the integer $L_w$ and the real constant $C_2$ of Hypothesis (fields and Galois data), subject to the requirements that this hypothesis imposes on them. The data $\mathfrak E$ *have the completion property for $k,m,t$* when the following holds. For every integer $b\ge0$ at which the data $\mathfrak E$ satisfy the field conditions and every choice of the remaining data, if $q>4tr+1$ and $d>4tr+1$, then there are data satisfying Hypothesis (fields and Galois data) that consist of $\mathfrak E$, the integers $k,m,t$, the integer $s_0=b$, the chosen remaining data, and an element $s_q$, an ideal $\mathfrak b_0$ and an embedding $\phi_0$.
