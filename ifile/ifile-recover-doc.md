#Recovery IFile

Recovery IFile dibutuhkan apabila ada laporan dari Toko bahwa mereka tidak bisa
menginput Do. Dilihat dari tipe-tipe laporan, tindakan yang dibutuhkan adalah
sebagai berikut:

##1. QTY Unmatch

Penyebab utama dari QTY Unmatch seringkali adalah tidak semua reference yang ada
pada dscoship digenerate oleh SAP. Misalnya saja dalam satu dscoship ada 10
reference/PO namun yang ada di IFile hanya ada 9 reference/PO.

Hal ini bisa terjadi karena 2 sebab:

1. Ada satu atau lebih reference yang ada di dalam dscoship memiliki MK negatif
atau sebab-sebab lain yang tidak sesuai dengan spesifikasi dscoship yang bisa
diproses oleh SAP. Bila hal ini terjadi, hubungi Ajay dan Nishant.

2. Semua PO/reference dalam dscoship sudah naik ke SAP dalam artian sudah
diproses namun tidak semua PO/reference dieksport ke IFile. Konon, hal ini
karena ada masalah locking. Untuk menyelesaikan hal ini kita dapat melakukan
recovery IFile dari sisi SAP dengan cara sbb:

	* Masuk ke vl03n, cari shipping document dengan cara memasukkan loading number
	* Copy IDoc seluruh PO/reference dalam shipping document tersebut.
	* Jalankan semua IDoc melalui tcode we19.

Ada kalanya kita tidak dapat menjalankan IDoc melalui we19 karena IDoc tersebut
sudah terhapus. Hal ini sering terjadi apabila toko melaporkan Do yang tidak
dapat diinput tersebut sudah lewat dari 3 (tiga) bulan. Untuk itu kita dapat
menggunakan cara sbb:

	* Masuk ke vl03n, cari semua reference/PO dalam shipping document.
	* untuk setiap reference/PO, edit document tersebut. Klik extras --> header lalu
	klik salah satu entry yang ada di dalam table yang ditampilkan. Klik repeat
output lalu simpan. File I akan teregenerate.

Cara terakhir memang efektif, namun saya tidak dapat menganjurkannya karena
nanti akan membuat IDoc baru sehingga ada duplikasi IDoc untuk satu dokumen
shipping yang sama.

##2. DO/Invoice Not Found

Bila hal ini yang dilaporkan oleh toko, maka ada dua kemungkinan yaitu:

1. SAP sudah menghasilkan IFile namun IFile tersebut tidak pernah sampai ke
toko.

Bila hal ini yang dilaporkan bisa jadi IFile yang dimaksud sudah ada di Nakulo.
Yang perlu kita lakukan adalah mencarinya di Nakulo. Gunakan IFile finder untuk
membantu proses ini.

2. SAP tidak mengenerate IFile.

Masalah ini adalah yang paling sering terjadi, dimana kita tidak bisa menemukan
IFile terdahulu di nakulo, namun shipping document bisa dicari di vl03n. Untuk
mengatasinya, kita bisa menggenerate ulang seperti pada step 1.1 di atas.

3. Shipping masih open atau belum diposting

Hal ini bisa diketahui bila kita dapat menemukan shipping document di tcode
vl03n namun tidak ada relationship. Untuk melakukan posting, edit shipping
document lalu klik Post Good Issue.

4. SAP belum mengenerate IFile karena dscoship belum naik.

Hal ini dapat diketahui dengan cara mencari shipping document di tcode vl03n
berdasarkan loading number seperti pada step 1.1 namun SAP memberitahu bahwa
tidak ada shipping document yang dimaksud.

Untuk mengatasi masalah ini, kita harus mengupload ulang file dscoship ke
ftp://cactus/ftpmgr2/_input/DC_SHIP. File dscoship untuk Infor bisa kita minta
dari pak Hadi Wibowo, sedangkan untuk DHL bisa dicari di
\\nakulo\393\RECEIVE\process.

Ingat setelah kita mendapatkan file discoship kita tidak dapat langsung
menguploadnya melainkan harus membersihkannya terlebih dahulu. Semua nomor
loading yang tidak kita butuhkan harus dihapus terlebih dahulu sebelum
mengupload ke cactus. Sebelum mengkopi ke cactus rename dulu file dscoship
tersebut dengan nama unik, misalnya saja dengan memberi tambahan _R1 atau _R2.
Bila kita lupa, file dscoship itu akan ditolak oleh SAP.

Setelah mengupload dscoship, tunggu 1-2 menit sampai file dscoship itu hilang
dari ftp://cactus/ftpmgr2/_input/DC_SHIP, lalu check hasil keluarannya di
ftp://cactus/ftpmgr2/_output/_BOSOUT/<store-code>.IFILE. Bandingkan Ifile ini
dengan dscoship, bila sudah sesuai kirim kabar bahwa toko sudah bisa input ulang
Do ini.
