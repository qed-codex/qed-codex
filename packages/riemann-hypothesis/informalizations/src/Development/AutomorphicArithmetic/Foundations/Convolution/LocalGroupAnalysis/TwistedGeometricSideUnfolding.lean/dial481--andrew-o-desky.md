---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/Convolution/LocalGroupAnalysis/TwistedGeometricSideUnfolding.lean",
  "declarations": [
    "UpperTheory.ConvolutionTheory.G.twistedGeometricSide_unfolding"
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

## Unfolding the twisted geometric sum into orbital integrals

[Theorem AGR.0953](https://andrewodesky.com/rh/lean/UpperTheory.ConvolutionTheory.G.twistedGeometricSide_unfolding/)

Let $G$ be a locally compact Hausdorff second countable topological group with Borel Haar measure $\mu$ that is also right invariant. Let $\Gamma\subseteq G$ be discrete and $\theta:G\to G$ a continuous homomorphism with $\theta(\Gamma)\subseteq\Gamma$. Let $f:G\to\mathbb C$ be continuous with compact support. Suppose there is a compact $C\subseteq G$ such that $$f(x^{-1}\delta\theta(x))\ne0,\quad\delta\in\Gamma\quad\Longrightarrow\quad x\in\Gamma C.$$ Choose a family $(r_i)_{i\in I}$ in $\Gamma$ containing a representative for each twisted conjugacy class meeting a nonzero value of $f$: for each $\delta\in\Gamma$ for which $f(x^{-1}\delta\theta(x))\ne0$ for some $x$, require $\delta=\gamma^{-1}r_i\theta(\gamma)$ for some $i,\gamma\in\Gamma$. Require also that $r_{i'}=\gamma^{-1}r_i\theta(\gamma)$ implies $i=i'$. Put $$\Gamma_i=\{\gamma\in\Gamma:\gamma^{-1}r_i\theta(\gamma)=r_i\}$$ and give every $\Gamma_i$ the discrete topology. Then every orbital integrand below is integrable, and the sum converges unconditionally to $$\sum_{i\in I}\int_{\Gamma_i\backslash G}f(x^{-1}r_i\theta(x))\,d\bar\mu_i(x) =\int_{\Gamma\backslash G}\sum_{\delta\in\Gamma}f(x^{-1}\delta\theta(x))\,d\bar\mu(x).$$
