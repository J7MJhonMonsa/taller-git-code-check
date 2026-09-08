# Guia paso a paso de Git y GitHub

Esta guia describe el flujo completo para trabajar en equipo, controlar versiones, enviar cambios a GitHub y realizar revisiones por pares mediante Pull Requests.

## 1. Configurar Git por primera vez

Ejecuta estos comandos una sola vez en tu equipo:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@example.com"
git config --global init.defaultBranch main
```

Verifica la configuracion:

```bash
git config --global --list
git --version
```

## 2. Obtener el repositorio

Si el repositorio ya existe en GitHub, clonalo:

```bash
git clone https://github.com/USUARIO/REPOSITORIO.git
cd REPOSITORIO
```

Verifica que el remoto sea correcto:

```bash
git remote -v
git status
```

Si estas creando un repositorio local nuevo:

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
```

## 3. Preparar el trabajo

Antes de comenzar una tarea, actualiza `main`:

```bash
git switch main
git pull origin main
```

Crea una rama para tu tarea y cambia a ella:

```bash
git switch -c nombre-de-la-tarea
```

Ejemplos:

```bash
git switch -c simulacion-ruido
git switch -c corrige-documentacion
git switch -c agrega-pruebas
```

Comprueba la rama actual:

```bash
git branch --show-current
git status
```

## 4. Crear y copiar directorios

En PowerShell puedes crear un directorio y copiar archivos asi:

```powershell
New-Item -ItemType Directory -Path datos
Copy-Item .\config.py .\datos\config.py
Copy-Item .\datos .\respaldo -Recurse
```

En Git Bash o Linux:

```bash
mkdir datos
cp config.py datos/config.py
cp -r datos respaldo
```

Despues revisa que Git detecte los cambios:

```bash
git status
git diff
```

## 5. Modificar archivos

Edita los archivos desde VS Code. Al terminar, revisa exactamente que cambio:

```bash
git status
git diff
```

Para revisar un archivo especifico:

```bash
git diff -- config.py
```

## 6. Guardar una version local

Anade un archivo especifico al siguiente commit:

```bash
git add config.py
```

Anade varios archivos:

```bash
git add config.py README.md
```

Anade todos los cambios del proyecto:

```bash
git add .
```

Revisa lo que esta preparado antes de confirmar:

```bash
git diff --cached
```

Crea el commit:

```bash
git commit -m "Describe brevemente el cambio"
```

Un commit es una version guardada localmente. Usa mensajes claros y realiza commits pequenos relacionados con una sola tarea.

Verifica el resultado:

```bash
git log -1 --oneline
git status
```

## 7. Enviar la rama a GitHub

La primera vez que subas una rama:

```bash
git push -u origin nombre-de-la-tarea
```

Por ejemplo:

```bash
git push -u origin simulacion-ruido
```

La opcion `-u` conecta la rama local con la rama remota. En los siguientes envios bastara con:

```bash
git push
```

GitHub puede solicitar autenticacion mediante un Personal Access Token (PAT) o SSH. Nunca escribas un token en el codigo, en un archivo o en una URL, y nunca lo compartas.

## 8. Crear un Pull Request en GitHub

Despues de ejecutar `git push`:

1. Abre el repositorio en GitHub.
2. Selecciona la rama que acabas de subir.
3. Pulsa **Compare & pull request**.
4. Comprueba que la rama destino sea `main`.
5. Escribe un titulo descriptivo.
6. Explica que cambiaste y como lo verificaste.
7. Pulsa **Create pull request**.
8. Solicita la revision de uno o mas companeros.

## 9. Revision por pares

La persona revisora debe comprobar:

- El cambio cumple el objetivo de la tarea.
- El codigo es legible y sigue el estilo del proyecto.
- No se suben tokens, contrasenas ni archivos temporales.
- Las pruebas o comandos de verificacion funcionan.
- La documentacion esta actualizada.
- El cambio no modifica partes ajenas sin necesidad.

Los comentarios deben ser concretos, respetuosos y accionables. Si se solicita una correccion, vuelve a la misma rama y ejecuta:

```bash
git add archivo-modificado.py
git commit -m "Corrige observaciones de la revision"
git push
```

El Pull Request se actualizara automaticamente con el nuevo commit.

## 10. Aceptar y fusionar el Pull Request

Cuando la revision este aprobada y las comprobaciones sean correctas:

1. Abre el Pull Request en GitHub.
2. Revisa los cambios y las aprobaciones.
3. Pulsa **Merge pull request**.
4. Pulsa **Confirm merge**.
5. Opcionalmente, pulsa **Delete branch** para eliminar la rama remota ya fusionada.

Al fusionar, los cambios de la rama pasan a `main`. El historial anterior de `main` no desaparece; Git conserva los commits anteriores.

## 11. Actualizar el repositorio local despues de la fusion

Despues de aceptar el Pull Request en GitHub, actualiza tu copia local:

```bash
git switch main
git pull origin main
```

Si quieres borrar la rama local que ya fue fusionada:

```bash
git branch -d nombre-de-la-tarea
```

Si tambien quieres borrarla de GitHub:

```bash
git push origin --delete nombre-de-la-tarea
```

## 12. Consultar el historial y comparar versiones

Ver todas las ramas y commits resumidos:

```bash
git log --oneline --graph --all
```

Ver un commit concreto:

```bash
git show ID_DEL_COMMIT
```

Comparar dos commits:

```bash
git diff ID_COMMIT_ANTERIOR ID_COMMIT_NUEVO
```

Descargar informacion remota sin fusionarla:

```bash
git fetch origin
```

## 13. Deshacer cambios de forma segura

Descartar cambios locales de un archivo que aun no esta confirmado:

```bash
git restore config.py
```

Quitar un archivo del area preparada sin borrarlo:

```bash
git restore --staged config.py
```

Deshacer un commit que ya fue compartido, conservando el historial:

```bash
git revert ID_DEL_COMMIT
git push
```

Para deshacer una fusion:

```bash
git switch main
git pull origin main
git revert -m 1 ID_DEL_COMMIT_DE_FUSION
git push
```

Tambien puedes abrir el Pull Request fusionado en GitHub y pulsar **Revert**. GitHub creara otro Pull Request para deshacer sus cambios.

Para revisar temporalmente una version anterior sin modificar una rama:

```bash
git switch --detach ID_DEL_COMMIT
```

Para regresar despues a `main`:

```bash
git switch main
```

Evita `git reset --hard` en `main` compartido, porque puede eliminar cambios locales y causar conflictos con otros colaboradores.

## 14. Archivos que no deben subirse

No subas credenciales, tokens, entornos virtuales ni archivos generados. Puedes incluirlos en `.gitignore`:

```gitignore
__pycache__/
*.pyc
.venv/
.env
```

Antes de crear un commit, verifica siempre:

```bash
git status
git diff --cached
```

## Flujo resumido para cada tarea

```bash
git switch main
git pull origin main
git switch -c nueva-tarea

# Editar archivos

git status
git diff
git add .
git commit -m "Describe el cambio"
git push -u origin nueva-tarea
```

Despues crea el Pull Request, solicita revision, corrige los comentarios si es necesario y fusiona en `main`. Finalmente actualiza tu copia local:

```bash
git switch main
git pull origin main
```
