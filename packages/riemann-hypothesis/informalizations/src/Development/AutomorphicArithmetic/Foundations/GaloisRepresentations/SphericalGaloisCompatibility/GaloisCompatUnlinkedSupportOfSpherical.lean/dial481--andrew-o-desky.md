---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/GaloisCompatUnlinkedSupportOfSpherical.lean",
  "declarations": [
    "UpperTheory.Gal.ToralGalois.galoisCompat_unlinkedSupport_of_spherical"
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

## Local comparison for unlinked character support

[Theorem AGR.0036](https://andrewodesky.com/rh/lean/UpperTheory.Gal.ToralGalois.galoisCompat_unlinkedSupport_of_spherical/)

Assume the universal weak-attachment and spherical-comparison assertion of ([Weak attachment and spherical comparison for polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.coreAll_of/)). Let $E$ be a CM field, $a\ge1$, $\ell$ prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and $\pi$ a regular algebraic polarized cuspidal representation of $\mathrm{GL}_a(\mathbb A_E)$. Let $r$ be any continuous semisimple representation weakly attached to $\pi$ in the sense defined there.

Let $v$ be finite, let $\sigma=\pi_v$, and suppose the supercuspidal support of $\sigma|\det|^{(1-a)/2}$ consists of rank-one characters, with no constituent equal to another constituent twisted by $|\det|$.

At $v\nmid\ell$, the Weil–Deligne parameter $x_v$ of $r$ has zero monodromy and equals the expected parameter $y_v=\operatorname{rec}(\sigma|\det|^{(1-a)/2})$, for every local correspondence satisfying the conditions described in ([Local support tests for zero-monodromy parameters](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Row.plainTor_of_tor/)).

At $v\mid\ell$, the restriction of $r$ is de Rham and potentially semistable. Its parameter has zero monodromy, and $$\det(T-x_v(g))=\det(T-y_v(g))\qquad(g\in W_{E_v}).$$ Its jumps at every induced embedding $\tau$ are any integer multiset mapping to $\{(a-1)/2-z:z\in\operatorname{Inf}_{\iota\tau}(\pi)\}$ in $\mathbb C$.
