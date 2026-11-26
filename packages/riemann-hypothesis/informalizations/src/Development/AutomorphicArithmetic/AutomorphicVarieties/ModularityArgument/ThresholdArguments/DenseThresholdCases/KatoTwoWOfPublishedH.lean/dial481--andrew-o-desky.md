---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KatoTwoWOfPublishedH.lean",
  "declarations": [
    "UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH"
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

## Vanishing of two rank-two Selmer groups

[Theorem GC.1118](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH/)

Assume the classical automorphy and descent package described in the conventions below. Write $\epsilon_\ell$ for the $\ell$-adic cyclotomic character and $G_F=\operatorname{Gal}(\overline F/F)$. Say a character factors through $M$ if it is trivial on automorphisms fixing every $M$-th root of unity.

The level condition $\mathcal L_\ell$, attachment to a newform, the comparison condition $\mathcal W^{\rm q}$ and the modularity condition $\mathcal M_e$ are defined in ([Level, attachment and comparison conditions on l-adic Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.Level/)).

Let $\ell$ be prime, $K$ an imaginary quadratic field inside $\overline{\mathbb Q}$, $e,N\in\mathbb N$, $\theta,\psi:G_{\mathbb Q}\to\overline{\mathbb Q}_\ell^\times$, and $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$. Put $\alpha=\epsilon_\ell^e\psi$. Assume all the following:

1. $\ell\ne2$, $e\ge1$, $\ell-1\nmid2e$, $N\ge1$ is even, $\gcd(N,|\operatorname{disc}K|)=1$, and $\ell\nmid|\operatorname{disc}K|h_K$, where $h_K$ is the class number.
2. $\ker\theta=G_K$ and $\theta^2=1$.
3. $\psi$ factors through $N$, has finite order prime to $\ell$, and $\psi^2=1$ on every inertia group above $\ell$.
4. There is a complex conjugation $c$ with $\alpha(c)=1$.
5. $\mathcal L_\ell(N|\operatorname{disc}K|;(e,-e);W)$ holds.
6. On one inertia group above $\ell$, after restriction to automorphisms fixing all roots of unity of some order $M\ge1$, the characteristic polynomial of $W(s)$ equals $(T-\epsilon_\ell(s)^e)(T-\epsilon_\ell(s)^{-e})$.
7. $\det W=\theta$. On every inertia group above $\ell$, $\operatorname{tr}W(s)=\alpha(s)+\alpha(s)^{-1}$, and for every $g\in G_{\mathbb Q}$, $$|\operatorname{tr}W(g)-\theta(g)\alpha(g)-\alpha(g)^{-1}|_\ell<1.$$
8. On some decomposition group above $\ell$, $W$ has an upper-triangular basis with diagonal characters whose inertia restrictions are $\epsilon_\ell^{e}\chi$ and $\epsilon_\ell^{-e}\chi$, where $\chi$ factors through $\ell$; that inertia group lies in $\ker\theta$.
9. $W$ restricted to $\ker(\epsilon_\ell|_{G_K})$ is irreducible.
10. There is an isomorphism of fields $\iota:\overline{\mathbb Q}_\ell\to\mathbb C$ for which $\mathcal M_e(\iota;W)$ holds: $W\otimes\epsilon_\ell^{-e}$ is attached to a newform of weight $2e+1$, and $\mathcal W^{\rm q}(\iota;W)$ holds.

Then $$H_f^1(\mathbb Q,W)=0,\qquad H_f^1(\mathbb Q,W\otimes\theta)=0:$$ for the action of $G_{\mathbb Q}$ on $\overline{\mathbb Q}_\ell^2$ through $W$, and for its action through $W\otimes\theta$, every continuous cocycle that satisfies the Selmer conditions is a coboundary, in the sense of ([Hypotheses on the points of the deformation rings of a sum of three characters](https://andrewodesky.com/rh/lean/UpperTheory.V.Th.RigidityFirstCase/)).
