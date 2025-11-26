package com.mycompany.principal;

import javax.swing.*;
import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class Principal extends JFrame {

    private static final String FILE_PATH =
            "C:\\Users\\ivans\\Documents\\POO 2025-2\\A6friends.txt";

    private long lastReadPosition = 0L;

    private JTextField txtName;
    private JTextField txtNumber;
    private JButton btnCreate;
    private JButton btnRead;
    private JButton btnUpdate;
    private JButton btnDelete;
    private JButton btnCleanFields;
    private JLabel jLabel1;
    private JLabel jLabel2;

    public Principal() {
        initComponents();
    }

    private void initComponents() {

        jLabel1 = new JLabel("Nombre");
        jLabel2 = new JLabel("Número");
        txtName = new JTextField();
        txtNumber = new JTextField();
        btnCreate = new JButton("Create");
        btnRead = new JButton("Read");
        btnUpdate = new JButton("Update");
        btnDelete = new JButton("Delete");
        btnCleanFields = new JButton("Clean Fields");

        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setTitle("Agenda de Amigos");

        btnCreate.addActionListener(e -> btnCreateActionPerformed());
        btnRead.addActionListener(e -> btnReadActionPerformed());
        btnUpdate.addActionListener(e -> btnUpdateActionPerformed());
        btnDelete.addActionListener(e -> btnDeleteActionPerformed());
        btnCleanFields.addActionListener(e -> btnCleanFieldsActionPerformed());

        GroupLayout layout = new GroupLayout(getContentPane());
        getContentPane().setLayout(layout);

        layout.setHorizontalGroup(
                layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createSequentialGroup()
                                .addGap(40, 40, 40)
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                                        .addComponent(jLabel1)
                                        .addComponent(jLabel2))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING, false)
                                        .addComponent(txtName, GroupLayout.PREFERRED_SIZE, 180, GroupLayout.PREFERRED_SIZE)
                                        .addComponent(txtNumber, GroupLayout.PREFERRED_SIZE, 180, GroupLayout.PREFERRED_SIZE))
                                .addContainerGap(40, Short.MAX_VALUE))
                        .addGroup(layout.createSequentialGroup()
                                .addGap(10, 10, 10)
                                .addComponent(btnCreate)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(btnRead)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(btnUpdate)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(btnDelete)
                                .addPreferredGap(LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(btnCleanFields)
                                .addGap(0, 10, Short.MAX_VALUE))
        );

        layout.setVerticalGroup(
                layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createSequentialGroup()
                                .addGap(40, 40, 40)
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                        .addComponent(jLabel1)
                                        .addComponent(txtName, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                        .addComponent(jLabel2)
                                        .addComponent(txtNumber, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                                .addGap(50, 50, 50)
                                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                                        .addComponent(btnCreate)
                                        .addComponent(btnRead)
                                        .addComponent(btnUpdate)
                                        .addComponent(btnDelete)
                                        .addComponent(btnCleanFields))
                                .addContainerGap(40, Short.MAX_VALUE))
        );

        pack();
        setLocationRelativeTo(null);
    }

    private void btnCleanFieldsActionPerformed() {
        txtName.setText("");
        txtNumber.setText("");
    }

    private void btnCreateActionPerformed() {
        try {
            String newName = txtName.getText().trim();
            String numberText = txtNumber.getText().trim();

            if (newName.isEmpty() || numberText.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Complete todos los campos.", "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            long newNumber = Long.parseLong(numberText);

            File file = new File(FILE_PATH);
            if (!file.exists()) {
                file.getParentFile().mkdirs();
                file.createNewFile();
            }

            RandomAccessFile raf = new RandomAccessFile(file, "rw");
            boolean found = false;

            while (raf.getFilePointer() < raf.length()) {
                String line = raf.readLine();
                if (line == null || line.isEmpty()) continue;

                String[] parts = line.split("!");
                if (parts.length < 2) continue;

                String name = parts[0];
                long number = Long.parseLong(parts[1]);

                if (name.equals(newName) || number == newNumber) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                raf.seek(raf.length());
                String newLine = newName + "!" + newNumber;
                raf.writeBytes(newLine + System.lineSeparator());
                JOptionPane.showMessageDialog(this, "Contacto añadido.");
            } else {
                JOptionPane.showMessageDialog(this, "El contacto ya existe.");
            }

            raf.close();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Error al crear contacto.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void btnReadActionPerformed() {
        try {
            String targetName = txtName.getText().trim();
            if (targetName.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Ingrese un nombre.", "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            File file = new File(FILE_PATH);
            if (!file.exists()) {
                JOptionPane.showMessageDialog(this, "El archivo no existe.", "Error", JOptionPane.ERROR_MESSAGE);
                return;
            }

            RandomAccessFile raf = new RandomAccessFile(file, "r");
            boolean found = false;

            raf.seek(lastReadPosition);

            while (raf.getFilePointer() < raf.length()) {
                String line = raf.readLine();
                if (line == null || line.isEmpty()) continue;

                String[] parts = line.split("!");
                if (parts.length < 2) continue;

                String name = parts[0];
                long number = Long.parseLong(parts[1]);

                if (name.equals(targetName)) {
                    txtNumber.setText(String.valueOf(number));
                    lastReadPosition = raf.getFilePointer();
                    found = true;
                    break;
                }
            }

            if (!found) {
                lastReadPosition = 0;
                JOptionPane.showMessageDialog(this, "Contacto no encontrado.");
            }

            raf.close();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Error al leer contacto.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void btnUpdateActionPerformed() {
        String targetName = txtName.getText().trim();
        String numberText = txtNumber.getText().trim();

        if (targetName.isEmpty() || numberText.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Complete ambos campos.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        File file = new File(FILE_PATH);
        if (!file.exists()) {
            JOptionPane.showMessageDialog(this, "El archivo no existe.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        File tempFile = new File(file.getAbsolutePath() + ".tmp");
        boolean found = false;

        try (RandomAccessFile raf = new RandomAccessFile(file, "r");
             RandomAccessFile tmp = new RandomAccessFile(tempFile, "rw")) {

            long newNumber = Long.parseLong(numberText);

            while (raf.getFilePointer() < raf.length()) {
                String line = raf.readLine();
                if (line == null || line.isEmpty()) continue;

                String[] parts = line.split("!");

                if (parts[0].equals(targetName)) {
                    tmp.writeBytes(targetName + "!" + newNumber + System.lineSeparator());
                    found = true;
                } else {
                    tmp.writeBytes(line + System.lineSeparator());
                }
            }

        } catch (Exception e) {
            tempFile.delete();
            JOptionPane.showMessageDialog(this, "Error al actualizar.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (found) {
            file.delete();
            tempFile.renameTo(file);
            lastReadPosition = 0;
            JOptionPane.showMessageDialog(this, "Contacto actualizado.");
        } else {
            tempFile.delete();
            JOptionPane.showMessageDialog(this, "No existe ese contacto.");
        }
    }

    private void btnDeleteActionPerformed() {
        String targetName = txtName.getText().trim();

        if (targetName.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Ingrese el nombre.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        File file = new File(FILE_PATH);
        if (!file.exists()) {
            JOptionPane.showMessageDialog(this, "El archivo no existe.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        File tempFile = new File(file.getAbsolutePath() + ".tmp");
        boolean found = false;

        try (RandomAccessFile raf = new RandomAccessFile(file, "r");
             RandomAccessFile tmp = new RandomAccessFile(tempFile, "rw")) {

            while (raf.getFilePointer() < raf.length()) {
                String line = raf.readLine();
                if (line == null || line.isEmpty()) continue;

                String[] parts = line.split("!");

                if (parts[0].equals(targetName)) {
                    found = true;
                } else {
                    tmp.writeBytes(line + System.lineSeparator());
                }
            }

        } catch (Exception e) {
            tempFile.delete();
            JOptionPane.showMessageDialog(this, "Error al eliminar.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (found) {
            file.delete();
            tempFile.renameTo(file);
            lastReadPosition = 0;
            txtName.setText("");
            txtNumber.setText("");
            JOptionPane.showMessageDialog(this, "Contacto eliminado.");
        } else {
            tempFile.delete();
            JOptionPane.showMessageDialog(this, "No existe ese contacto.");
        }
    }

    public static void main(String[] args) {
        try {
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception ignored) {}

        java.awt.EventQueue.invokeLater(() -> new Principal().setVisible(true));
    }
}
