---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/EisensteinTranslationProducts/EllipticOnePole.lean",
  "declarations": [
    "Formalism.L2.Th1.F.ellipticNoPole",
    "Formalism.L2.Th1.F.pDerivZero",
    "Formalism.L2.Th1.F.pInjective",
    "Formalism.L2.Th1.F.sigmaAdd",
    "Formalism.L2.Th1.F.sigmaOrder"
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

## The Weierstrass sigma addition formula

[Theorem ANT.0224](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.sigmaAdd/)

Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$, and put $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$. Use the functions $\sigma_\Lambda$, $S$ and the operators $U_x$ defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)). Let $\wp_\Lambda$ be the Weierstrass elliptic function of $\Lambda$.

For $z,w\in\mathbb C\setminus\Lambda$, $$\sigma_\Lambda(z+w)\sigma_\Lambda(z-w)=-\sigma_\Lambda(z)^2\sigma_\Lambda(w)^2\bigl(\wp_\Lambda(z)-\wp_\Lambda(w)\bigr).$$

Write $\sigma^*=S$ and $\wp=\wp_\Lambda$. For $P,Q,z\in\mathbb C$ satisfying $Q\notin\Lambda$ and $z+P\notin\Lambda$, $$U_{P+Q}\sigma^*(z)\,U_{P-Q}\sigma^*(z)=\bigl(U_Q\sigma^*(0)\bigr)^2\bigl(\wp(Q)-\wp(z+P)\bigr)\bigl(U_P\sigma^*(z)\bigr)^2.$$

## A periodic meromorphic function without poles is constant

[Theorem AV.0473](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.ellipticNoPole/)

Let $\Lambda\subset\mathbb C$ be the lattice of a pair of real-linearly independent periods. Let $f:\mathbb C\to\mathbb C$ be meromorphic at every point, periodic under $\Lambda$, and satisfy $\operatorname{ord}_z(f)\ge0$ for every $z\in\mathbb C$. There is $c\in\mathbb C$ such that $f(z)=c$ at every point where $f$ is continuous.

## Fibres of the Weierstrass function

[Theorem AV.0497](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.pInjective/)

Let $\Lambda\subset\mathbb C$ be the lattice of a pair of real-linearly independent complex periods, and let $\wp_\Lambda$ be its Weierstrass function, defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)). For $z,w\in\mathbb C\setminus\Lambda$, $$\wp_\Lambda(z)=\wp_\Lambda(w)\quad\Longleftrightarrow\quad z-w\in\Lambda\ \text{or}\ z+w\in\Lambda.$$

## Orders of zeros of a translated sigma function

[Theorem ANT.0532](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.sigmaOrder/)

Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$, and put $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$. Let $\sigma_\Lambda$ be the Weierstrass sigma function defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)). For every $a,b,z\in\mathbb C$ with $a\ne0$, $$\operatorname{ord}_z\bigl(\sigma_\Lambda(a\,\cdot+b)\bigr)=\begin{cases}1,&az+b\in\Lambda,\\0,&az+b\notin\Lambda.\end{cases}$$

## Zeros of the derivative of the Weierstrass function

[Theorem ANT.0541](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.pDerivZero/)

Let $\Lambda\subset\mathbb C$ be the lattice of two complex periods linearly independent over $\mathbb R$, and let $\wp_\Lambda$ be its Weierstrass function, defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)). For every $z\in\mathbb C\setminus\Lambda$, $$\wp_\Lambda'(z)=0\quad\Longleftrightarrow\quad2z\in\Lambda.$$
