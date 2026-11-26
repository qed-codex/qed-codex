---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/KatoTwoOfUseN.lean",
  "declarations": [
    "UpperTheory.V.Z.Kato.Used"
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

## A rank-two Selmer vanishing assumption with auxiliary quadratic fields

[Definition / hypothesis GC.D072](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Kato.WeilSphericalRecords.KatoTwoW/)

Let $\ell$ be an odd prime, $\Omega$ an algebraic closure of $\mathbb Q$, $K\subset\Omega$ an imaginary quadratic field, $e\ge1$ and $N\ge1$ an even integer. Suppose $\ell-1$ does not divide $2e$, $\ell$ does not divide $|\operatorname{disc}K|h_K$, and $N$ is coprime to $|\operatorname{disc}K|$. Let $G=\operatorname{Gal}(\Omega/\mathbb Q)$, let $\theta,\psi:G\to\overline{\mathbb Q}_\ell^\times$ be characters, and let $W:G\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ be a representation. Write $\chi_\ell$ for the cyclotomic character. Assume that $\ker\theta=\operatorname{Gal}(\Omega/K)$ and $\theta^2=1$, and that $\psi$ has order prime to $\ell$ and satisfies $\psi^2=1$ on each inertia group above $\ell$. For some complex conjugation $c$, assume $\chi_\ell(c)^e\psi(c)=1$.

The data must also satisfy conditions on roots of unity, the level and ordinary polynomial of $W$, a local flag at $\ell$, and irreducibility (not expanded). In addition, $\det W=\theta$; on inertia at $\ell$ the trace of $W$ is $\chi_\ell^e\psi+(\chi_\ell^e\psi)^{-1}$; and for every $g\in G$, $$\bigl|\operatorname{tr}W(g)-\theta(g)\chi_\ell(g)^e\psi(g)-(\chi_\ell(g)^e\psi(g))^{-1}\bigr|_\ell<1.$$

Fix an isomorphism $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$. Suppose that a newform of weight $2e+1$ has $W\otimes\chi_\ell^{-e}$ as its associated representation: the representation is semisimple, and at almost all primes it is unramified and the characteristic polynomial of inverse Frobenius, transported by $\iota$, is the Hecke polynomial of the newform. The newform and its Hecke polynomial are subject to the definitions in item (10) of ([Hypothesis list D: fifteen assumed statements on cuspidal automorphic representations of general linear groups, base change, descent to unitary groups and Galois representations](https://andrewodesky.com/rh/lean/UpperTheory.V.Af.HypothesesH'/)).

Suppose further that for every quadratic CM extension $M/\mathbb Q$ inside $\Omega$ on which $W$ restricts irreducibly, the restriction satisfies a local potential-unramifiedness condition and an automorphic window condition (not expanded).

The assumption asserts that, for every such choice of data and isomorphism, the Bloch–Kato Selmer groups of $W$ and $W\otimes\theta$ vanish. Here vanishing means that every continuous first cocycle satisfying the unramified local condition away from $\ell$ and the finite local condition at $\ell$ is a coboundary; the finite local condition at $\ell$ is not expanded.
