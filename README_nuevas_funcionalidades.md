# 📚 Nuevas Funcionalidades - Producción Oral

## ✨ Mejoras Implementadas

### 1. 📄 Visualización Mejorada de Documentos
- **PDFs profesionales** con diseño optimizado para impresión
- **Visor integrado** para PDFs dentro del navegador
- **Soporte para TXT/RTF** con formato automático
- **Tipografía mejorada** usando Georgia serif para mejor legibilidad

### 2. 🎨 PDFs con Diseño Profesional
Los nuevos PDFs incluyen:
- **Márgenes generosos** para impresión
- **Diseño por secciones con colores**:
  - 🟡 Objetivos (amarillo)
  - 🟢 Actividades (verde)
  - 🟣 Mini serie (morado)
  - 🔵 Tareas (azul)
  - 🩷 Evaluación (rosa)
- **Tipografía profesional** y jerarquía visual clara
- **Formato A4 optimizado** para impresión

### 3. 💾 Opciones Múltiples de Descarga
Cada sesión ofrece:
- **📄 Ver en navegador**: Abre el PDF en el visor integrado
- **🔗 Abrir en nueva pestaña**: Abre en pestaña separada
- **💾 Descargar directamente**: Descarga el archivo al dispositivo

### 4. 📋 Contenido de las Sesiones Disponibles

#### Sesión 1: Presentaciones y situación inicial
- Objetivos: Presentaciones, nivel B2.1, proyecto mini serie
- Actividades: Círculo de presentaciones, entrevistas, personajes
- Mini serie: "La llegada al aeropuerto"

#### Sesión 2: Debate: ¿Mudarse a España?
- Objetivos: Expresar opiniones, vocabulario ventajas/desventajas
- Actividades: Torbellino de ideas, debate estructurado, mini-debates
- Mini serie: "La decisión de mudarse"

#### Sesión 3: Situación: Buscar piso en Granada
- Objetivos: Vocabulario de vivienda, negociación, simulaciones
- Actividades: Vocabulario visual, llamadas, visitas a pisos
- Mini serie: "La primera visita al piso"
- Vocabulario específico granadino incluido

## 🛠️ Características Técnicas

### Visor de Documentos
- **Responsive**: Se adapta a móviles y tablets
- **Full-screen**: Experiencia inmersiva de lectura
- **Navegación táctil**: Zoom y scroll intuitivos
- **Mantenimiento del estado**: No pierdes tu lugar al cambiar de tamaño

### Generador de PDFs
- **HTML5 + CSS3**: Tecnología moderna de generación
- **Chrome Headless**: Renderizado de alta calidad
- **Optimización de tamaño**: PDFs ligeros (~230KB)
- **Codificación UTF-8**: Soporte completo para caracteres españoles

## 📂 Estructura de Archivos

```
Produccion-Oral/
├── index.html                 # Web mejorada
├── materials/
│   ├── cuadernos/
│   │   ├── S1_Produccion_Oral.pdf    # ✨ Nuevo PDF profesional
│   │   ├── S2_Produccion_Oral.pdf    # ✨ Nuevo PDF profesional
│   │   ├── S3_Produccion_Oral.pdf    # ✨ Nuevo PDF profesional
│   │   ├── S1_Presentaciones_Inicial.txt     # Original
│   │   ├── S2_Debate_Mudarse.txt            # Original
│   │   └── S3_Buscar_Piso.txt               # Original
│   └── guia-docente.pdf
├── pdf_generator.html         # ✨ Generador de PDFs
└── README_nuevas_funcionalidades.md  # Este archivo
```

## 🎯 Cómo Usar

### Para Estudiantes
1. **Accede a la web**: Abre `index.html` en tu navegador
2. **Selecciona sesión**: Haz clic en los chips de la sección "Guía del curso"
3. **Elige formato**:
   - Click en "📄 Ver en navegador" para lectura online
   - Click en "💾 Descargar directamente" para guardar PDF
4. **Imprime si necesario**: Los PDFs están optimizados para impresión

### Para Profesores
1. **Generar más PDFs**: Usa `pdf_generator.html` con el parámetro `?session=S4`
2. **Personalizar contenido**: Edita `sessionData` en el generador
3. **Mantenimiento**: Los archivos originales (.txt) permanecen como backup

## 🔄 Actualizaciones Futuras

### Pendientes
- [ ] Generar PDFs para sesiones 4-13
- [ ] Añadir more functionality interactivity
- [ ] Integrar con plataforma del centro
- [ ] Añadir quizzes autoevaluativos

### Mejoras Técnicas
- [ ] Progressive Web App (PWA)
- [ ] Offline functionality
- [ ] Accessibility improvements (WCAG 2.1)
- [ ] Multi-language support

## 📞 Soporte

Si encuentras algún problema:
1. **Recarga la página**: Muchos problemas se resuelven con refresh
2. **Verifica conexión**: Los PDFs necesitan conexión para cargarse
3. **Navegador compatible**: Chrome, Firefox, Safari, Edge (versiones recientes)
4. **Contacta al profesor**: Javier Benítez Láinez

---

**© 2024-2025 Producción e Interacción Oral — Nivel 7 (B2.1)**
**Universidad de Granada - Centro de Lenguas Modernas**