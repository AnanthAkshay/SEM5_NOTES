# Machine Learning (IS51) Mathematical Formula & Numerical Verification Log

**Audit Date:** 14 October 2026  
**Scope:** Machine Learning (24IS51) Unit 3 (Regression Portion — CIE-1 Scope)  
**Evaluator:** Academic Verification & Code Quality Suite  

---

## 1. Unit 3 Theoretical Formula Audit

| Topic | Prescribed Mathematical Formulation | Verification Status | Notes / Fixes Applied |
|---|---|---|---|
| **Simple Linear Regression Model** | $y = \beta_0 + \beta_1 x + \epsilon = mx + c + \epsilon$ | **VERIFIED** | Formulated with standard Gauss-Markov error assumptions ($E[\epsilon]=0, \text{Var}(\epsilon)=\sigma^2, \text{Cov}(\epsilon_i, \epsilon_j)=0$). |
| **OLS Cost Function** | $\text{RSS} = S(m, c) = \sum_{i=1}^n (y_i - (m x_i + c))^2$ | **VERIFIED** | Matches sum of squared vertical residuals minimization. |
| **OLS Closed-Form Slope** | $m = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2}$ | **VERIFIED** | Equivalent algebraic expressions verified across both centered and raw summation forms. |
| **OLS Closed-Form Intercept** | $c = \bar{y} - m\bar{x}$ | **VERIFIED** | Guarantees regression line passes through centroid $(\bar{x}, \bar{y})$. |
| **Multiple Linear Regression** | $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$ | **VERIFIED** | Matrix dimensions: $\mathbf{y} \in \mathbb{R}^{n \times 1}$, $\mathbf{X} \in \mathbb{R}^{n \times (p+1)}$, $\boldsymbol{\beta} \in \mathbb{R}^{(p+1) \times 1}$. |
| **Normal Equations** | $\mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{X}^T\mathbf{y} \implies \boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ | **VERIFIED** | Requires $\mathbf{X}$ to have full column rank ($p+1$). |
| **Polynomial Regression** | $\phi(x) = [1, x, x^2, \dots, x^d]^T, \quad \hat{y} = \boldsymbol{\beta}^T\phi(x)$ | **VERIFIED** | Linear in parameters $\boldsymbol{\beta}$, non-linear in feature $x$. |
| **Ridge Regression ($L_2$)** | $J(\boldsymbol{\beta}) = \frac{1}{2n}\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_2^2$ | **VERIFIED** | Closed form: $\boldsymbol{\beta}_{\text{Ridge}} = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$. Invertibility guaranteed for $\lambda > 0$. |
| **Lasso Regression ($L_1$)** | $J(\boldsymbol{\beta}) = \frac{1}{2n}\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_1$ | **VERIFIED** | Produces exact sparsity ($\beta_j = 0$ for non-informative features). |
| **Gradient Descent Update** | $\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \alpha \nabla_{\boldsymbol{\beta}} J(\boldsymbol{\beta})$ | **VERIFIED** | Gradient $\nabla_{\boldsymbol{\beta}} J = -\frac{1}{n}\mathbf{X}^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})$. |
| **Logistic Regression Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | **VERIFIED** | Squashes $(-\infty, +\infty)$ to $(0, 1)$. Derivative $\sigma'(z) = \sigma(z)(1 - \sigma(z))$. |
| **Odds Ratio & Logit** | $\text{Odds} = \frac{p}{1-p} = e^z, \quad \text{Logit}(p) = \ln(\text{Odds}) = \mathbf{w}^T\mathbf{x} + b$ | **VERIFIED** | Canonical link function for Bernoulli distribution. |
| **Binary Cross-Entropy Loss** | $J(\mathbf{w}) = -\frac{1}{n} \sum_{i=1}^n [y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{p}_i)]$ | **VERIFIED** | Convex with respect to weights $\mathbf{w}$. |
| **Evaluation Metrics** | $\text{MAE} = \frac{1}{n}\sum \|y_i - \hat{y}_i\|, \quad \text{MSE} = \frac{1}{n}\sum (y_i - \hat{y}_i)^2$ | **VERIFIED** | $\text{RMSE} = \sqrt{\text{MSE}}, \quad R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$. |
| **Adjusted $R^2$** | $R^2_{\text{adj}} = 1 - \left[\frac{(1 - R^2)(n - 1)}{n - p - 1}\right]$ | **VERIFIED** | Penalizes model complexity / degrees of freedom. |

---

## 2. Numerical Problem Verification Results

### Problem 1: Ramaiah CIE-1 March 2026 Q1(c) — Study Hours vs Exam Marks
- **Dataset:** $X = [2, 4, 6, 8, 10]$, $Y = [50, 60, 65, 80, 85]$ ($n=5$)
- **Calculations:**
  - $\bar{X} = 30 / 5 = 6.00$, $\bar{Y} = 340 / 5 = 68.00$
  - $\sum (X - \bar{X})^2 = (-4)^2 + (-2)^2 + 0^2 + 2^2 + 4^2 = 40.00$
  - $\sum (X - \bar{X})(Y - \bar{Y}) = (-4)(-18) + (-2)(-8) + 0(-3) + 2(12) + 4(17) = 72 + 16 + 0 + 24 + 68 = 180.00$
  - **Slope ($b$):** $180.00 / 40.00 = \mathbf{4.5000}$
  - **Intercept ($a$):** $68.00 - (4.5000)(6.00) = 68.00 - 27.00 = \mathbf{41.0000}$
  - **Regression Equation:** $\hat{Y} = 4.50X + 41.00$
  - **Prediction for $X = 7$ hours:** $\hat{Y}(7) = 4.50(7) + 41.00 = \mathbf{72.50\text{ marks}}$
  - **Fit Statistics:** $\text{SSE} = 20.00, \text{SST} = 830.00 \implies R^2 = 1 - (20/830) = \mathbf{0.9759\text{ (97.59\%)}}$
- **Status:** **PASS** (100% verified against automated test suite `audit/verify/ml/verify_ml_u3.py`).

### Problem 2: Faculty Practice Handout — Ice Cream Sales vs Temperature
- **Dataset:** $X = [20, 22, 24, 26, 28, 30, 32, 34]$, $Y = [120, 135, 150, 165, 180, 195, 210, 225]$ ($n=8$)
- **Calculations:**
  - $\sum X = 216 \implies \bar{X} = 27.00$, $\sum Y = 1380 \implies \bar{Y} = 172.50$
  - $\sum X^2 = 6000$, $\sum XY = 38520$
  - **Slope ($b$):** $\frac{8(38520) - (216)(1380)}{8(6000) - (216)^2} = \frac{308160 - 298080}{48000 - 46656} = \frac{10080}{1344} = \mathbf{7.5000}$
  - **Intercept ($a$):** $172.50 - (7.5000)(27.00) = 172.50 - 202.50 = \mathbf{-30.0000}$
  - **Regression Equation:** $\hat{Y} = -30.0000 + 7.5000X$
  - **Prediction for $X = 29^\circ\text{C}$:** $\hat{Y}(29) = -30.00 + 7.50(29) = \mathbf{187.50\text{ units}}$
- **Status:** **PASS**.

### Problem 3: Ridge vs OLS Regularization Shrinkage
- **Given:** $\sum x_i^2 = 100$, $\sum x_i y_i = 400$, $\lambda = 20$
- **Calculations:**
  - $\beta_{\text{OLS}} = 400 / 100 = \mathbf{4.0000}$
  - $\beta_{\text{Ridge}} = 400 / (100 + 20) = 400 / 120 = \mathbf{3.3333}$ (16.7% shrinkage)
- **Status:** **PASS**.

---

## 3. Automated Verification Suites

- `audit/verify/ml/verify_ml_u1.py`: **ALL PASS** (Descriptive statistics, outlier detection, Pearson correlation, spam classifier, medical classifier).
- `audit/verify/ml/verify_ml_u2.py`: **ALL PASS** (PCA covariance matrix, eigenvalues, Find-S algorithm, Candidate-Elimination, PAC sample complexity).
- `audit/verify/ml/verify_ml_u3.py`: **ALL PASS** (OLS regression slope/intercept, $R^2$, Logistic sigmoid probability, odds ratio).
