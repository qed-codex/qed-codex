---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/EisensteinTranslationProducts/QuasiPeriodConstUnique.lean",
  "declarations": [
    "Formalism.L2.Th1.F.opUComm",
    "Formalism.L2.Th1.F.th0Basic"
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

## Commutator of normalized complex translations

[Theorem AV.0749](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.opUComm/)

Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$ and put $$A=|\operatorname{Im}(\overline{\omega_1}\omega_2)|,\qquad H(z,w)=z\overline w/A,\qquad E(z,w)=\operatorname{Im}H(z,w).$$ For every function $f:\mathbb C\to\mathbb C$ define $$U_xf(z)=f(z+x)\exp\left(-\pi H(z,x)-\frac\pi2H(x,x)\right).$$ Then $$U_0f=f,\qquad U_xU_yf(z)=e^{-2\pi iE(x,y)}U_yU_xf(z)\qquad(x,y,z\in\mathbb C).$$

## A normalized even theta function at a half period

[Theorem ANT.0763](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.th0Basic/)

Let $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\subset\mathbb C$, where $\omega_1,\omega_2$ are linearly independent over $\mathbb R$. Let $S$ and $h$ be the normalized sigma function and Hermitian form defined in ([Sigma functions and translations on a period lattice](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)).

Let $\omega_0\in\Lambda$ with $t=\omega_0/2\notin\Lambda$, and define $$\Theta_t(z)=\frac{S(z+t)}{S(t)}e^{-\pi h(z,t)}.$$ Then $\Theta_t$ is entire, $\Theta_t(0)=1$, $\Theta_t(-z)=\Theta_t(z)$, and $$\Theta_t(z)=0\quad\Longleftrightarrow\quad z+t\in\Lambda.$$ For every $\omega\in\Lambda$ and $z\in\mathbb C$, $$\Theta_t(z+\omega)=\varepsilon(\omega)e^{\pi i\operatorname{Im}h(\omega,\omega_0)}e^{\pi h(z,\omega)+\pi h(\omega,\omega)/2}\Theta_t(z),$$ where $\varepsilon(\omega)=1$ if $\omega/2\in\Lambda$ and $\varepsilon(\omega)=-1$ otherwise.
