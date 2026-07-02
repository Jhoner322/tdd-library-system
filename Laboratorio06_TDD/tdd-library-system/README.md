# Sistema de Gestión de Biblioteca - TDD Básicos

Este proyecto consiste en la implementación de un sistema básico automatizado utilizando la metodología **Desarrollo Guiado por Pruebas (Test Driven Development - TDD)** y el framework `pytest`.

## 🚀 Metodología TDD Aplicada

El desarrollo se realizó siguiendo el ciclo estricto de TDD:
1. **Fase Roja (Red):** Se escribieron primero las pruebas unitarias en `test_payment_service.py` definiendo el comportamiento esperado y las reglas de negocio, las cuales fallaron inicialmente.
2. **Fase Verde (Green):** Se implementó el código mínimo necesario en `library_service.py` para lograr que todas las pruebas pasen de forma satisfactoria.
3. **Refactorización (Refactor):** Se limpió y ordenó el código para asegurar buenas prácticas de programación sin alterar su comportamiento.

## 📋 Reglas de Negocio Validadas

El sistema controla tres escenarios principales:
* **Cálculo de Totales con Impuestos:** Se aplica un impuesto del 18% (`TAX = 0.18`) a los montos procesados de forma correcta.
* **Validación de Montos Negativos:** El sistema arroja un error de tipo `ValueError` si se intenta ingresar un valor menor a cero.
* **Límite Diario de Operaciones:** Se bloquea cualquier proceso que supere el límite máximo establecido (`DAILY_LIMIT = 10000`).

## 🛠️ Instalación y Ejecución

Sigue estos pasos para clonar el proyecto y ejecutar las pruebas en tu entorno local:

1. **Instalar las dependencias requeridas (pytest):**
   ```bash
   pip install pytest