---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/EvenThetaFunctionCmLatticeIntegralSplitPrimeStatement.lean",
  "declarations": [
    "GlobalTheory.T.evenThetaFunction_cmLattice_integral_splitPrime"
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

## Integral moments of the normalized CM theta function at a split prime

[Theorem PHT.0787](https://andrewodesky.com/rh/lean/GlobalTheory.T.evenThetaFunction_cmLattice_integral_splitPrime/)

Fix the source's full CM arithmetic datum with imaginary quadratic field $K$, discriminant parameter $d$ and chosen complex embedding. Let $\mathfrak c\subset\mathcal O_K$ be a nonzero ideal with $\gcd(N\mathfrak c,2d)=1$. Choose $\delta\in\mathbb C$ with $$\delta^{12}=\operatorname{disc}(\mathfrak c),\qquad \Lambda=\delta\mathfrak c\subset\mathbb C,$$ using the embedding and the lattice discriminant normalization below. Fix the source's theta-lattice realization of $\Lambda$, and let $G$ be its normalized even theta function defined below, with the normalization of ([A normalized even theta function at a half period](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.th0Basic/)). Let $q\ne2$ be prime with $$\left(\frac{-d}{q}\right)=1,\qquad\gcd(N\mathfrak c,q)=1.$$ Let $\iota:\mathbb C\simeq\mathbb C_q$ be a field isomorphism. Suppose $(\delta_0,\theta,\Omega)$ satisfies the normalized period conditions below, using the torsion-translation identities and coefficient bounds in ([A unit p-adic period for translated CM theta functions](https://andrewodesky.com/rh/lean/GlobalTheory.MomOne.GenusOne.thetaLaws_unit_period/)). For every finite set $I$ and every family $v_i\in\Lambda$, there exists a continuous $\mathbb C_q$-linear functional $$\mu:C(\mathbb Z_q^I,\mathbb C_q)\to\mathbb C_q,\qquad\|\mu\|\le1,$$ such that, putting $u_i=\iota^{-1}(\Omega/\iota(\delta_0))v_i$, for every $k\ge0$ and $j:\{1,\ldots,k\}\to I$, $$\iota\bigl(D^kG(0)[u_{j(1)},\ldots,u_{j(k)}]\bigr) =\mu\left(a\mapsto\prod_{\ell=1}^k a_{j(\ell)}\right).$$
