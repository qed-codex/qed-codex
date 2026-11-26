---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/BiextensionNondegenerateModMaximalIdealIntegralC.lean",
  "declarations": [
    "GlobalTheory.AlphaPair.nonDeg_of_polAt"
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

## A tangent nondegeneracy condition for the special-fibre cubical pairing

[Theorem PHT.1031](https://andrewodesky.com/rh/lean/GlobalTheory.AlphaPair.nonDeg_of_polAt/)

Let $E$ be a CM number field with the CM arithmetic data specified in the conventions of ([Nonzero Gram determinant and bases away from finitely many primes](https://andrewodesky.com/rh/lean/GlobalTheory.T.gram_det_ne_zero_local_basis_cofinite/)). Let $V$ be a complete discrete valuation ring of characteristic zero, and let $(G,L)$ be the semiabelian datum below over $V$. Suppose the generic fibre of $G$ is proper and $L$ on that fibre is relatively ample with trivial translation kernel. Let $\Omega$ be algebraically closed of characteristic $p>0$, and let $\beta:V\to\Omega$ kill the maximal ideal. Write $G_\Omega$ for the special fibre and $e_p$ for the cubical Weil pairing associated to $L$.

Consider a family $u_A(a)\in G_\Omega(A)$, defined for every commutative $\Omega$-algebra $A$ and $a\in A$ with $a^p=0$, natural under $\Omega$-algebra maps and satisfying $u_A(a+a')=u_A(a)+u_A(a')$. Assume that whenever $A$ has an augmentation $\rho:A\to\Omega$ with nilpotent kernel, $a^2=0$, and $z\in G_\Omega(A)[p]$ reduces to the identity, one has $$e_p(u_A(a),z)=1.$$ Then $$u_{\Omega[\varepsilon]/(\varepsilon^2)}(\varepsilon)=0.$$
