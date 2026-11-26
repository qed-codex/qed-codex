---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AutomorphyUnramifiedCoefficients.lean",
  "declarations": [
    "UpperTheory.V.Aut.AutBAlt",
    "UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt",
    "UpperTheory.V.Aut.LemWAlt"
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

## An automorphy assumption for specializations with unramified coefficients

[Definition / hypothesis AGR.D103](https://andrewodesky.com/rh/lean/UpperTheory.V.Aut.AutomorphyUnramifiedCoefficientsAlt/)

This page states one hypothesis of the theorem ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)). It concerns the deformation rings defined in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)), for coefficient rings $\mathcal O$ that are unramified over $\mathbb Z_\ell$. It provides the element $g_1$ at which these rings are formed, and it asserts that a subring of each of them is finite over $\mathcal O$ and that the representations obtained from them satisfy conditions of automorphy.

**Setting.** Let $K$, $\ell$, $\mathcal O$, $N$, $e$, $\psi$ and a datum $\mathfrak D$ for them, with its character $\eta$ and its complex conjugation $c$, be as in ([Deformation rings of a sum of three characters with a sign character](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)); in particular $K$ is an imaginary quadratic field and conditions 1–4 of ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)) hold. That page defines the marked pairs $(c,g_1)$, the universal lifts $(R^{\rm loc},r^{\rm loc})$, the deformation rings $(S,r_S)$ of $\mathfrak D$ at an element $g_1\in G_{\mathbb Q}$, the subalgebras $S_0\subset E_S\subset S$, the homomorphisms $G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ obtained from $r_S$ by a homomorphism $\xi:E_S\to\overline{\mathbb Q}_\ell$, their matrix parts $\dot r$, conditions (I) and (II), and the homomorphisms that extend the corner of $r$. The conditions $\mathcal A_K$ and $\mathcal M_e$ are defined in ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

**The assumption.** Let $K$, $\ell$, $\mathcal O$, $N$, $e$, $\psi$ and $\mathfrak D$ be any data as above such that $$\operatorname{length}_{\mathcal O}(\mathcal O/\ell\mathcal O)=1,$$ and let $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ be any isomorphism of fields. Then there is an element $g_1\in G_{\mathbb Q}$ with the following four properties.

1. The pair $(c,g_1)$ is marked.
2. For every universal lift $(R^{\rm loc},r^{\rm loc})$ and every deformation ring $(S,r_S)$ of $\mathfrak D$ at $g_1$ formed with it, the $\mathcal O$-algebra $S_0$ is finitely generated as an $\mathcal O$-module.
3. Let $(S,r_S)$ be such a deformation ring, let $\xi:E_S\to\overline{\mathbb Q}_\ell$ be a homomorphism of $\mathcal O$-algebras, and let $r:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ be a homomorphism obtained from $r_S$ by $\xi$. If $r$ satisfies condition (I), then $\mathcal A_K(\iota;\rho\otimes\epsilon_\ell^{-1})$ holds for the representation $\rho=\dot r|_{G_K}$ of $G_K$.
4. Let $(S,r_S)$, $\xi$ and $r$ be as in property 3. If $r$ satisfies condition (II) and $\dot r(g)_{22}=1$ for every $g\in G_K$, then every homomorphism $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ that extends the corner of $r$ satisfies $\mathcal M_e(\iota;W)$.
