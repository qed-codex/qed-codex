---
{
  "module": "src/Formalism/LocalToGlobal/Columns/CoefficientsModP/PairingNondegenerateHolds.lean",
  "declarations": [
    "Formalism.L2.DIV.pairingPositive_holds"
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

## Positive definiteness of the normalized polynomial Weyl pairing

[Theorem REP.0312](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.pairingPositive_holds/)

Let $K$ be a field with involution, $\varphi:K\to\mathbb C$ a field homomorphism, $I$ a finite set, and $n\ge0$ an integer. For each $\tau\in I$, let $\lambda_\tau\in\mathbb Z^n$ be weakly decreasing and let $G_\tau\in M_n(K)$ satisfy $\varphi(G_\tau)>0$ as a complex Hermitian matrix.

For $n>0$ put $d_\tau=\lambda_{\tau,n}$ and $\nu_{\tau,j}=\lambda_{\tau,j}-d_\tau$; for $n=0$ put $d_\tau=0$ and let $\nu_\tau$ be the empty list. Use the modules $\nabla_{\nu_\tau}(K)$ and highest-weight polynomials $H_\tau=v_{\nu_\tau}$ of ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)), in independent $n\times n$ variable blocks $Z_\tau$.

For each field and shifted weight, use the fixed polynomial basis specified by the polynomial-basis construction in ([Polynomial coefficient representations and integral lattices](https://andrewodesky.com/rh/lean/Formalism.IndefR.Bridge.CoefMapTie/)). Let $(b_T)_T$ be the products of these basis vectors across the independent blocks. Then $$\left(\varphi(B_G(b_T,b_{T'}))\right)_{T,T'}$$ is positive definite.
