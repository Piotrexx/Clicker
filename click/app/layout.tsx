import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import NavBar from "@/components/navbar/page";
import { Pixelify_Sans } from "next/font/google";

const pixel = Pixelify_Sans({
  subsets: ['latin'],
  display: 'swap',
})

export const metadata: Metadata = {
  title: "CLICKER",
  description: "CLICKER",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={pixel.className}>
        {children}
        </body>
    </html>
  );
}
