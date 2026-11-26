---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof/HolomorphicContinuation/MollifiedIntegrability/ContinuousCexpIp.lean",
  "declarations": [
    "PositivityTheory.Rg.Sw.WR.D.mollId"
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

## An integral formula for a pushforward density

[Theorem ANT.1213](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.Sw.WR.D.mollId/)

Let $n\ge0$, let $E=\operatorname{Mat}_n(\mathbb R)$ with pairing $\langle y,z\rangle=\sum_{a,b}y_{ab}z_{ab}$ and its usual Lebesgue measure, and let $(X,\mu)$ be a measure space with $\mu$ s-finite. Let $\Psi:X\to\mathbb C$ be integrable, let $q:X\to E$ be measurable, and let $t\in\mathbb R\setminus\{0\}$. Suppose $$F(y)=\int_X\Psi(x)e^{it\langle y,q(x)\rangle}\,d\mu(x)$$ is integrable on $E$. Then for every continuous compactly supported $\psi:E\to\mathbb C$, $$\int_X\psi(q(x))\Psi(x)\,d\mu(x)=\int_E\psi(\beta)\left(\frac{|t|}{2\pi}\right)^{n^2}\left(\int_EF(y)e^{-it\langle\beta,y\rangle}\,dy\right)d\beta.$$
