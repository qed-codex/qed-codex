---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars/SymmetricSquareMixedCharpoly.lean",
  "declarations": [
    "UpperTheory.symmetric_square_mixed_charpoly"
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

## Characteristic polynomials of a mixed four-dimensional representation

[Theorem REP.0390](https://andrewodesky.com/rh/lean/UpperTheory.symmetric_square_mixed_charpoly/)

Let $k$ be a field with $2\ne0$, let $j:\Gamma_0\hookrightarrow\Gamma$ be an injective homomorphism with image of index two, and let $t\notin j(\Gamma_0)$. Let $\alpha,\beta\in k^\times$, $\rho:\Gamma_0\to\mathrm{GL}_2(k)$ and $R:\Gamma\to\mathrm{GL}_4(k)$ satisfy $$\rho(u)=\operatorname{diag}(\alpha^2,\beta^2)\quad\text{whenever }j(u)=t^2,$$ $$R(j(h))=M_{\beta/\alpha}(\rho(h),\rho(h'))\quad\text{whenever }j(h')=t^{-1}j(h)t,$$ $$R(t)=\operatorname{diag}(\beta,-\alpha,-\beta,\alpha).$$ For every $s\notin j(\Gamma_0)$, $$\det(T-R(j(g)))=\det(T-\rho(g))\det(T-\rho(g'))$$ whenever $j(g')=s^{-1}j(g)s$, and $$\det(T-R(s))=\det(T^2-\rho(g))\quad\text{whenever }j(g)=s^2.$$
