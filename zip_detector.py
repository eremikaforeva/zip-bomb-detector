import zipfile
import os

def analyze_zip(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as z:
            total_compressed = 0
            total_uncompressed = 0
            file_count = 0
            nested_zips = 0

            for info in z.infolist():
                total_compressed += info.compress_size
                total_uncompressed += info.file_size
                file_count += 1

                if info.filename.endswith('.zip'):
                    nested_zips += 1

            # Avoid division by zero
            if total_compressed == 0:
                ratio = 0
            else:
                ratio = total_uncompressed / total_compressed

            print(f"\n[+] Analysis for: {file_path}")
            print(f"Files inside: {file_count}")
            print(f"Compressed size: {total_compressed} bytes")
            print(f"Uncompressed size: {total_uncompressed} bytes")
            print(f"Compression ratio: {ratio:.2f}")
            print(f"Nested ZIPs: {nested_zips}")

            # 🚨 Detection logic
            if ratio > 100:
                print("[!] Suspicious: High compression ratio")
            if total_uncompressed > 1_000_000_000:  # 1GB
                print("[!] Suspicious: Huge uncompressed size")
            if nested_zips > 5:
                print("[!] Suspicious: Too many nested ZIPs")
            if file_count > 10000:
                print("[!] Suspicious: Too many files")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    path = input("Enter path to ZIP file: ").strip()
    
    if os.path.exists(path):
        analyze_zip(path)
    else:
        print("File not found.")
