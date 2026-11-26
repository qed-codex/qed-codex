---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/RigEnd3.lean",
  "declarations": [
    "UpperTheory.V.Th.RigidityFirstCase",
    "UpperTheory.V.Th.RigiditySecondCase"
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

## Hypotheses on the points of the deformation rings of a sum of three characters

[Definition / hypothesis AGR.D097](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.RigidityFirstCase/)

This page states three hypotheses of the theorem ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)). Each concerns the local points of the deformation rings defined in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)): the first two assert the vanishing of Selmer groups of adjoint representations at these points, and the third places the representations of the points in a class of automorphic representations.

**Vanishing of $H^1_f$.** Let $\overline{\mathbb Q}$ be an algebraic closure of $\mathbb Q$, $G_{\mathbb Q}=\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$, $\ell$ a prime and $G_{\mathbb Q_\ell}=\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell)$. Let $V$ be a finite-dimensional vector space over $\overline{\mathbb Q}_\ell$, with its $\ell$-adic topology, and let $G_{\mathbb Q}$ act on $V$ by linear maps. A *cocycle* is a continuous map $a:G_{\mathbb Q}\to V$ with $a(gh)=a(g)+g\,a(h)$ for all $g,h$, and a *coboundary* is a map $g\mapsto gx-x$ with $x\in V$. A cocycle $a$ satisfies the *Selmer conditions* if the following two conditions hold.

1. For every prime $p\ne\ell$ there are a place $A$ of $\overline{\mathbb Q}$ above $p$ and an element $x\in V$ with $a(s)=sx-x$ for every $s$ in the inertia group of $A$.
2. There is an embedding of fields $j:\overline{\mathbb Q}\to\overline{\mathbb Q}_\ell$ for which the following holds. Let $D_j$ be the group of pairs $(g,s)\in G_{\mathbb Q}\times G_{\mathbb Q_\ell}$ with $s\circ j=j\circ g$; it acts on $V$ through $g$ and on the crystalline period ring $B_{\rm cris}$ through $s$. Then there is $z\in V\otimes_{\mathbb Q_\ell}B_{\rm cris}$ with $$a(g)\otimes1=(g,s)z-z\qquad\text{for all }(g,s)\in D_j.$$

We write $H^1_f(\mathbb Q,V)=0$ if every cocycle that satisfies the Selmer conditions is a coboundary. Here $B_{\rm cris}$ is the ring that carries the structure of Fontaine's crystalline period ring in local period data for the prime $\ell$, in the sense of ([Local period rings and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LocRings/)); one choice of local period data is used for each $\ell$.

**Setting of the hypotheses.** Let $K$, $\ell$, $\mathcal O$, $N$, $e$, $\psi$, a datum $\mathfrak D$ with its character $\eta$ and its complex conjugation $c$, a universal lift $(R^{\rm loc},r^{\rm loc})$, an element $g_1\in G_{\mathbb Q}$ such that $(c,g_1)$ is marked, a deformation ring $(S,r_S)$ of $\mathfrak D$ at $g_1$ formed with $(R^{\rm loc},r^{\rm loc})$, and a local point $f$ of $S$ be as in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)), with the homomorphism $r_f:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ and the representation $\rho_f$ of $G_K$. Let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields. Conditions (I) and (II), the adjoint action $\operatorname{ad}r_f$ and the homomorphisms that extend the corner of $r_f$ are defined on that page. The conditions $\mathcal A_K$ and $\mathcal M_e$ and the class $\mathcal R_1(\iota,e,N)$ are defined in ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

Each of the following three hypotheses is the assertion that its statement holds for all these data.

**Hypothesis (P1): rigidity at irreducible automorphic points.** If $r_f$ satisfies condition (I) and $\mathcal A_K(\iota;\rho_f\otimes\epsilon_\ell^{-1})$ holds, then $H^1_f(\mathbb Q,M_3(\overline{\mathbb Q}_\ell))=0$ for the adjoint action $\operatorname{ad}r_f$ of $G_{\mathbb Q}$ on $M_3(\overline{\mathbb Q}_\ell)$.

**Hypothesis (P2): rigidity at points of block form.** Suppose that $r_f$ satisfies condition (II), and let $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ be a continuous homomorphism that extends the corner of $r_f$ and satisfies $\det W=\eta$ and $\mathcal M_e(\iota;W)$. Then $H^1_f(\mathbb Q,M_2(\overline{\mathbb Q}_\ell))=0$ for every linear action of $G_{\mathbb Q}$ on $M_2(\overline{\mathbb Q}_\ell)$ of the following kind: there are a complex conjugation $c'\in G_{\mathbb Q}$ and a matrix $P\in\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ such that $${}^tW(s)\,P\,W(c'sc'^{-1})=P,\qquad s\cdot X=W(s)\,X\,W(s)^{-1},\qquad c'\cdot X=-P^{-1}\,{}^tX\,P$$ for all $s\in G_K$ and $X\in M_2(\overline{\mathbb Q}_\ell)$.

**Hypothesis (P3): irreducible automorphic points belong to $\mathcal R_1$.** If $r_f$ satisfies condition (I) and $\mathcal A_K(\iota;\rho_f\otimes\epsilon_\ell^{-1})$ holds, then $\rho_f\in\mathcal R_1(\iota,e,N)$.
