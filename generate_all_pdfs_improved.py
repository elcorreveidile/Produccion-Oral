#!/usr/bin/env python3
import subprocess
import os
import time
import sys

# Lista de sesiones a generar
sessions_to_generate = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13']

def generate_pdf_for_session(session):
    """Generar PDF mejorado para una sesión específica"""
    print(f"🔄 Generando PDF mejorado para {session}...")

    cmd = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless',
        '--disable-gpu',
        '--disable-extensions',
        '--no-sandbox',
        '--disable-popup-blocking',
        '--disable-translate',
        '--disable-background-timer-throttling',
        '--disable-renderer-backgrounding',
        '--disable-backgrounding-occluded-windows',
        '--print-to-pdf=output.pdf',
        '--print-to-pdf-no-header',
        '--virtual-time-budget=30000',
        f'file://{os.getcwd()}/pdf_generator_improved.html?session={session}'
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            # Mover el PDF generado al nombre correcto
            pdf_name = f'materials/cuadernos/{session}_Produccion_Oral_Mejorado.pdf'

            # Eliminar el PDF anterior si existe
            if os.path.exists(pdf_name):
                os.remove(pdf_name)

            os.rename('output.pdf', pdf_name)
            print(f"✅ PDF mejorado generado: {pdf_name}")
            return True
        else:
            print(f"❌ Error generando PDF para {session}: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Chrome no encontrado. Asegúrate de que Chrome esté instalado.")
        return False
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout generando PDF para {session}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado con {session}: {str(e)}")
        return False

def main():
    print("🚀 Generando PDFs mejorados para todas las sesiones...")
    print("=" * 60)

    # Verificar que existe el archivo generador mejorado
    if not os.path.exists('pdf_generator_improved.html'):
        print("❌ No se encuentra el archivo 'pdf_generator_improved.html'")
        return False

    success_count = 0
    total_sessions = len(sessions_to_generate)

    for i, session in enumerate(sessions_to_generate, 1):
        print(f"\n({i}/{total_sessions}) Procesando {session}...")

        if generate_pdf_for_session(session):
            success_count += 1

        # Pequeña pausa entre generaciones para evitar sobrecarga
        time.sleep(2)

    print("\n" + "=" * 60)
    print(f"✨ Proceso completado:")
    print(f"   ✅ Éxitos: {success_count}/{total_sessions}")
    print(f"   ❌ Fallos: {total_sessions - success_count}/{total_sessions}")

    if success_count == total_sessions:
        print("🎉 Todos los PDFs se generaron correctamente!")

        # Verificar archivos generados
        print("\n📋 Verificando archivos generados:")
        for session in sessions_to_generate:
            pdf_file = f'materials/cuadernos/{session}_Produccion_Oral_Mejorado.pdf'
            if os.path.exists(pdf_file):
                size = os.path.getsize(pdf_file)
                print(f"   ✅ {pdf_file} ({size:,} bytes)")
            else:
                print(f"   ❌ {pdf_file} - NO ENCONTRADO")
    else:
        print("⚠️ Algunos PDFs no se pudieron generar. Revisa los errores arriba.")

    return success_count == total_sessions

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)